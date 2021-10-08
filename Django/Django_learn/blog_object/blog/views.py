import json
import os


from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import Count, functions, F
from django.db import transaction
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup

from blog.myforms import Userform
from blog.utils.validcode import valid_code
from blog.models import *
from blog_object import settings
# Create your views here.

def valid_code_func(request):
    '''处理生成验证码的请求'''
    data = valid_code(request)
    return HttpResponse(data)


def main_func(request):
    articles = Article.objects.all()
    return render(request, 'main.html', locals())


def login_func(request):
    if request.method == 'POST':

        response = {'user': None, 'msg': None}
        usn = request.POST.get('usn')
        pwd = request.POST.get('pwd')
        vcode = request.POST.get('vcode')
        print(vcode, request.session.get('vcode'))
        if vcode.upper() == request.session.get('vcode').upper():
            user = auth.authenticate(username=usn, password=pwd)
            if user:
                auth.login(request, user)
                response['user'] = usn
            else:
                response['msg'] = '用户名或者密码错误'
        else:
            response['msg'] = '验证码错误'
        return JsonResponse(response)

    return render(request, 'login.html')


def register_func(request):

    if request.is_ajax():
        print(request.POST)
        response = {'user': None, "msg": None, 'clndata':None}
        form = Userform(request.POST)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)

            response['user'] = form.cleaned_data.get('usn')
            # 保存用户数据到user库
            usn = form.cleaned_data.get('usn')
            pwd = form.cleaned_data.get('pwd')
            email = form.cleaned_data.get('email')
            headimg = request.FILES.get('headimg')

            extra = {}
            if headimg:   # 防止用户上传空值
                extra['avatar'] = headimg
            UserInfo.objects.create_user(username=usn, password=pwd, email=email, **extra)

        else:
            print(form.cleaned_data)
            print(form.errors)
            response['clndata'] = form.cleaned_data
            response['msg'] = form.errors
        return JsonResponse(response)
        
    form = Userform()
    return render(request, 'register.html', locals())


def logout_func(request):
    auth.logout(request)
    return redirect('/login/')


@login_required  # 验证登录，如果已经登陆，返回页面，不然跳转到settings配置的login_url网址
def home_func(request, username, **kwargs):
    user = UserInfo.objects.filter(username=username).first()
       # 当前用户所有文章

    if not user:
        return render(request, 'not_found.html')
    article_list = user.article_set.all()
    if kwargs:
        if kwargs['condition'] == 'category':
            article_list = article_list.filter(category__title=kwargs['param'])
        elif kwargs['condition'] == 'tag':
            article_list = article_list.filter(tags__title=kwargs['param'])
        elif kwargs['condition'] == 'archive':
            year = kwargs['param'].split('-')[0]
            month = kwargs['param'].split('-')[1]
            article_list = article_list.filter(create_time__year=year, create_time__month=month)

    return render(request, 'home.html', locals())


def article_detail_func(request, username, article_id):
    article_detail = Article.objects.filter(pk=article_id).first()
    commment_list = Comment.objects.filter(article_id=article_id).all()
    return render(request, 'article_detail.html', locals(),)


def updown_func(request):
    use_id = request.user.pk
    print(request.POST)
    response = {"state": True, 'handled': None}
    if request.method == 'POST':
        choice = json.loads(request.POST.get('choice'))
        article_id = request.POST.get('article_id')

        # 判断点赞表中是否有记录
        obj = ArticleUpDown.objects.filter(user_id=use_id, article_id=article_id).first()

        if not obj:
            ArticleUpDown.objects.create(is_up=choice, article_id=article_id, user_id=use_id)
            if choice:
                Article.objects.filter(pk=article_id).update(up_count=F('up_count') + 1)
            else:
                Article.objects.filter(pk=article_id).update(up_count=F('down_count') + 1)

        else:
            response['state'] = False
            response['handled'] = obj.is_up
        return JsonResponse(response)


def comment_func(request):
    print(request.POST)
    article_id = request.POST.get('article_id')
    pid = request.POST.get('pid')
    uid = request.user.pk
    content = request.POST.get('content')
    article_obj = Article.objects.filter(pk=article_id).first()

    # 事务操作，同进同退，防止出现，上面插入下面报错没插入的情况
    with transaction.atomic():
        com_obj = Comment.objects.create(content=content, article_id=article_id,  parent_comment_id=pid, user_id=uid)
        Article.objects.filter(pk=article_id).update(comment_count=F('comment_count')+1)

    response = {}
    response['create_time'] = com_obj.create_time.strftime('%Y-%m-%d %X')
    response['username'] = request.user.username
    response['content'] = content

    # 发送邮件
    send_mail(
        subject=f'您的文章{article_obj.title}新增了一条评论',
        message=content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['850635521@qq.com'],

    )
    return JsonResponse(response)


def comment_tree_func(request):
    article_id = request.GET.get('article_id')
    ret = Comment.objects.filter(article_id=article_id).values("pk", "content", "parent_comment_id")
    ret = list(ret)
    return JsonResponse(ret, safe=False)


@login_required
def manage_func(request):
    article_list = Article.objects.filter(user=request.user)
    return render(request, 'backend/backend.html', locals())


@login_required
def add_article_func(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 防止xss攻击,过滤script标签
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup.find_all():

            print(tag.name)
            if tag.name == "script":
                tag.decompose()  # 删除标签

        # 构建摘要数据,获取标签字符串的文本前150个符号

        desc = soup.text[0:150] + "..."

        Article.objects.create(title=title, desc=desc, content=str(soup), user=request.user)
        return redirect("/manage/")

    return render(request, 'backend/add_article.html', locals())

def upload_func(request):
    print(request.FILES)
    file_obj = request.FILES.get('upload_img')

    path = os.path.join(settings.MEDIA_ROOT, 'add_files', file_obj.name)
    with open(path, 'wb') as f:
        for line in file_obj:
            f.write(line)

    response = {
        "error": 0,
        "url": f'/media/add_files/{file_obj.name}'
    }
    print(response)

    return JsonResponse(response, safe=False)

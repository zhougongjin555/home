import random
import time
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Avg, Max, Min, Count, Q
from django.core.paginator import Paginator, EmptyPage
from django import forms
from django.contrib import auth
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from book_management.models import *


class UserForms(forms.Form):
    usn = forms.CharField(min_length=6, label='用户名',
                          widget=widgets.TextInput(attrs={'class': 'form-control'}))   # 设置表单规则
    pwd = forms.CharField(min_length=6, label='密码',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    pwd1 = forms.CharField(min_length=6, label='确认密码',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱',
                          widget=widgets.EmailInput(attrs={'class': 'form-control'}))
    # phone = forms.CharField(label='电话',
    #                       widget=widgets.TextInput(attrs={'class': 'form-control'}))

    def clean_usn(self):  # 一定要是clean_开头才行
        val = self.cleaned_data.get("usn")  # 从通过初步校验的数据中找到usn字段
        ret = User.objects.filter(username=val)

        if not ret:
            return val
        else:
            raise ValidationError('该用户已经注册')

    # def clean_tel(self):
    #     tel = self.cleaned_data.get('tel')
    #
    #     if len(tel) == 11:
    #         return tel
    #     else:
    #         raise ValidationError('手机号不满足11位')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        pwd1 = self.cleaned_data.get('pwd1')
        if pwd and pwd1:
            if pwd == pwd1:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")  # 存放在errors{"__all__":"msg"}
        else:
            return self.cleaned_data

def page(request, is_anonymous, num, cpage, content=None):  # requset对象， 是否登录， 分页数

    book_list = Book.objects.values("title", 'publishDate', 'price', 'authors__name', 'publish__name')  # 反向查询用表名

    if content:
        num = 50
        book_list = book_list.filter(Q(authors__name=content) | Q(publish__name=content))
    paginator = Paginator(book_list, num)
    nums = paginator.num_pages

    if nums > 9:
        if cpage <= 5:
            page_range_num = range(1, 10)
        elif cpage >= nums-4:
            page_range_num = range(nums-8, nums+1)
        else:
            page_range_num = range(cpage-4, cpage+5)
    else:
        page_range_num = paginator.page_range

    try:
        page_content = paginator.page(cpage)
        # for i in page_content:
        #     print(i)
    except EmptyPage as e:
        page_content = paginator.page(1)
    return {"page_content": page_content, 'page_range_num': page_range_num, 'paginator': paginator}



def confirm_data(request):
    bookname = request.POST.get('bookname')
    book = Book.objects.filter(title=bookname)
    print("-----------------",request.POST.get('publish'),request.POST.get('city'),request.POST.get('email'))
    if book:
        message = '书籍已经存在'
        print(message)
        return HttpResponse(message)
    else:

        ret = Publish.objects.create(name=request.POST.get('publish'), city=request.POST.get('city'), email=request.POST.get('email'))
        print(ret, ret.nid)
        book = Book.objects.create(title=bookname,
                            publishDate=request.POST.get('publishDate'),
                            price=request.POST.get('price'),
                            publish_id=ret.nid,
                            )
        aret = Author.objects.create(name=request.POST.get('author'))
        book.authors.add(aret)
        message = '添加成功'
        return HttpResponse(message)


def add_func(request):
    usn = request.user.username
    is_user = request.user.is_anonymous
    print(is_user,'---------------')
    if not is_user:
        return render(request, 'add.html', locals())
    else:
        return HttpResponse('还未登录，不能操作')


def insertdata_func(request):
    Author.objects.create(name='周公瑾', age=18)
    Author.objects.create(name='诸葛亮', age=55)
    Author.objects.create(name='关云长', age=66)
    Author.objects.create(name='张翼德', age=22)
    print('author done...')
    Publish.objects.create(name='人民出版社', city='北京市', email='885521@qwe.com')
    Publish.objects.create(name='杭州出版社', city='杭州市', email='112233@qwe.com')
    Publish.objects.create(name='日本出版社', city='日本市', email='777555@qwe.com')
    Publish.objects.create(name='美国出版社', city='美国省', email='666666@qwe.com')
    print('publish done...')
    # 批量插入数据库
    book_list = []
    a = 1355772380
    b = 1529772380
    for i in range(100):
        publisher = random.randint(1, 4)    #随机出版社
        author_id = random.randint(1, 4)       #随机作者id
        author = Author.objects.filter(nid=author_id).first()   # 找作者id的作者
        rtime = time.localtime(random.randint(a, b))
        rtime = time.strftime('%Y-%m-%d', rtime)            # 随机出版日期
        book_obj = Book.objects.create(title=f'book{i}', publishDate=rtime, price=i+100, publish_id=publisher)    # 生成book记录
        book_obj.authors.add(author)            # 关连多对多表
    #     book = Book(title=f'book{i}', publishDate=rtime, price=i + 100, publish_id=publisher)  # 实例化对象
    #     book_list.append(book)   # 批量加入数据
    # Book.objects.bulk_create(book_list)
    print('book done...')
    return HttpResponse('插入100本书，四个作者，四个出版社')


def select(request):
    return redirect('/main/')


def register_func(request):
    '''注册用户'''
    form = UserForms()
    if request.method == 'POST':
        print(request.POST)
        # return HttpResponse('200 OK')

        form = UserForms(request.POST)
        # print(form)
        if form.is_valid():
            print('校验成功')
            print(form.cleaned_data)
            # UserInfo.objects.create(usn=request.POST.get('usn'),
            #                         pwd=request.POST.get('usn'),
            #                         email=request.POST.get('email'),
            #                         phone=request.POST.get('phone'))
            User.objects.create_user(username=request.POST.get('usn'),
                                    password=request.POST.get('pwd'),
                                    email=request.POST.get('email'))
            return redirect("/login/")

        else:
            print('校验失败')
            # print(form.cleaned_data)
            # print("失败信息", form.errors)
            # print('email失败信息', form.errors.get('email')[0])

            error_all = form.errors.get('__all__')
            # print("error", form.errors.get("__all__")[0])
            print(error_all)
            return render(request, 'register.html', locals())


    return render(request, 'register.html', locals())


def login_func(request):
    '''登录账户'''
    if request.method == 'POST':
        usn = request.POST.get('usn')
        pwd = request.POST.get('pwd')
        print(usn, pwd)
        user = auth.authenticate(username=usn, password=pwd)
        print(user)
        if user:
            auth.login(request, user)  # 实现操作 request.user = user
            return redirect('/main/')
        # user = UserInfo.objects.filter(usn=usn, pwd=pwd)
        # print(user)
        # if user:
        #     response = HttpResponse('200 OK')
        #     response.set_cookie('is_login', True)
        #     response.set_cookie('username', usn)
        # else:
        #     msg = '账号或者密码错误'
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误'})
    return render(request, 'login.html')


def logout_func(request):
    '''注销账户'''
    auth.logout(request)
    return redirect('/main/')


def main_func(request):
    is_anonymous = request.user.is_anonymous
    if not is_anonymous:
        print(is_anonymous)
        cpage = int(request.GET.get('page', 1))
        pages_attr = page(request, is_anonymous, 10, cpage)
        page_content, page_range_num, paginator = pages_attr.get('page_content'), pages_attr.get(
            'page_range_num'), pages_attr.get('paginator')
        return render(request, 'main.html', locals())
    else:
        return redirect('/login/')

def select_func(request):
    content = request.POST.get('search') or request.COOKIES.get('search')  # 两者取其中之一
    is_anonymous = request.user.is_anonymous
    if not is_anonymous:
        cpage = int(request.GET.get('page', 1))
        pages_attr = page(request, is_anonymous, 10, cpage, content)
        page_content, page_range_num, paginator = pages_attr.get('page_content'), pages_attr.get('page_range_num'), pages_attr.get('paginator')
        response = render(request, "search.html", locals())
        # if content:
        #     response.set_cookie('search', content, path='/select_book/')
        return response
    else:
        return redirect('/login/')

def delete_func(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        print(bookname)
        book = Book.objects.filter(title=bookname).delete()
    is_anonymous = request.user.is_anonymous
    if not is_anonymous:
        cpage = int(request.GET.get('page', 1))
        pages_attr = page(request, is_anonymous, 10, cpage)
        page_content, page_range_num, paginator = pages_attr.get('page_content'), pages_attr.get(
            'page_range_num'), pages_attr.get('paginator')
        return render(request, "delete.html", locals())
    else:
        return redirect('/login/')

def edit_func(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        oldauthor = request.POST.get('oldauthor')
        author = request.POST.get('author')
        price = request.POST.get('price')
        publishDate = request.POST.get('publishDate')
        publish = request.POST.get('publish')
        print(bookname, oldauthor, author, price, publishDate, publish)
        # 找出版社和作者的id
        modified_publish = Publish.objects.filter(name=publish).values('nid')
        newauthor = Author.objects.filter(name=author).first()

        # 找不到创建
        if not modified_publish:
            Publish.objects.create(name=publish)
            modified_publish = Publish.objects.filter(name=publish).values('nid')
        if not newauthor:
            Author.objects.create(name=author)
            newauthor = Author.objects.filter(name=author).first()

        # 修改表记录
        book = Book.objects.filter(title=bookname)
        book.update(publishDate=publishDate, price=price, publish_id=modified_publish)  # 修改表记录
        book.first().authors.clear()   # 清楚原有的多对多对应关系
        book.first().authors.add(newauthor)  # 添加新的对应关系


    is_anonymous = request.user.is_anonymous
    if not is_anonymous:
        cpage = int(request.GET.get('page', 1))
        pages_attr = page(request, is_anonymous, 10, cpage)
        page_content, page_range_num, paginator = pages_attr.get('page_content'), pages_attr.get(
            'page_range_num'), pages_attr.get('paginator')
        return render(request, "edit.html", locals())
    else:
        return redirect('/login/')
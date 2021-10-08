import random
import time
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Avg, Max, Min, Count
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


def add_func(requesr):

    # 生成一条记录
    # Publish.objects.create(name='人民出版社', city='北京', email='885521@ad.com')
    # Publish.objects.create(name='南京出版社', city='南京', email='8asdasd1@asd.cn')

    # 方式1
    # Book.objects.create(title='金瓶梅', publishDate='2001-5-23', price=130, publish_id=1)

    # 方式2

    # pub_obj = Publish.objects.filter(nid=1).first()
    # Book.objects.create(title="三国演绎", price=150, publishDate="2012-12-12", publish=pub_obj)
    # book_obj = Book.objects.create(title='西游记', publishDate='1950-2-2', price=330, publish=pub_obj)
    # print(book_obj.publish_id, book_obj.publish) # .publish返回的是一个对象

    # 查询西游记的出版社对应的邮箱
    # book_obj = Book.objects.filter(title="西游记").first()
    # print(book_obj.publish.email)
    # print(book_obj.authors.all())

    # 绑定多对多的关系
    # zhou = Author.objects.get(name='周公瑾')
    # zhu = Author.objects.get(name='诸葛亮')

    # book_obj.authors.add(zhou, zhu)  # authors是django自动创建的多对多数据库返回的对象

    # 解除多对多的关系
    # book_obj.authors.remove(zhu)    # 移除对象
    # book_obj.authors.clear() # 清除所有的包含该对象的记录

    # 查询主键为4的书籍的所有作者的名字
    # book = Book.objects.filter(nid=3).first()
    # print(book.authors.all())  # [obj1,obj2...] queryset: 与这本书关联的所有作者对象集合
    # ret = book.authors.all().values("name")
    # print(ret)



    return HttpResponse('200 OK')


def query_func(request):
    """
        跨表查询:
           1 基于对象查询
           2 基于双下划线查询
           3 聚合和分组查询
           4 F 与 Q查询
        :param request:
        :return:
        """
    # -------------------------基于对象的跨表查询(子查询)-----------------------
    '''
        正向查询： 关联属性在A表中，A-->B ，按照字段查询
        反向查询： 关联属性在B表中，A-->B ，按照 “表名小写 + _set” 查询
    '''

    # 一对多查询：##########################################################################
    # 一对多查询的正向查询 : 查询金瓶梅这本书的出版社的名字
    # book_obj = Book.objects.filter(title="金瓶梅").first()
    # print(book_obj.publish) # 与这本书关联出版社对象
    # print(book_obj.publish.name)

    # 一对多查询的反向查询 : 查询人民出版社出版过的书籍名称
    # publish = Publish.objects.filter(name="人民出版社").first()
    # ret = publish.book_set.all()
    # print(ret)


    # 多对多查询: ##########################################################################
    # 正向查询:
    # 需求: 通过Book表join与其关联的Author表,属于正向查询:按字段authors通知ORM引擎join book_authors与author
    # ret = Book.objects.filter(title="金瓶梅")
    # print(ret.authors.all())

    # 反向查询
    # 找“周公瑾”写的所有的书籍
    # ret = Author.objects.filter(name='周公瑾')
    # print(ret.book_set.all())

    # 一对一查询：##########################################################################
    # 正向查询：按照字段
    # ret = Author.objects.filter(name='周公瑾').first()
    # addr = ret.authorDetail.addr
    # print(addr)

    # 反向查询：按照表明小写
    # ret = AuthorDetail.objects.filter(birthday='2021-08-24').first()
    # print(ret.author.name)



    # -------------------------基于双下划线的跨表查询(join查询)-----------------------
    # 一对多查询：##########################################################################
    # 一对多查询的正向查询 : 查询金瓶梅这本书的出版社的名字
    # 方式1
    # book_obj1 = Book.objects.filter(title="西游记").values("publish__name")  # values("表名__查询的字段")
    # print(book_obj1)
    # 方式2
    # book_obj2 = Publish.objects.filter(book__title="西游记").values("name")
    # print(book_obj2)


    # 多对多查询: ##########################################################################
    # 正向查询:
    # 需求: 通过Book表join与其关联的Author表,属于正向查询:按字段authors通知ORM引擎join book_authors与author
    # 方式1
    # ret = Book.objects.filter(title="西游记").values('authors__name')  # values("多对多对象__查询的字段")
    # print(ret)
    # 方式2
    # ret = Author.objects.filter(book__title="西游记").values('name')
    # print(ret)



    # 一对一查询：##########################################################################
    # 正向查询：按照字段
    # 1
    # ret = Author.objects.filter(name='周公瑾').values('authordetail__telephone')
    # print(ret)
    # 2
    # ret = AuthorDetail.objects.filter(author__name='周公瑾').values('telephone')
    # print(ret)

    # 连续跨表：##########################################################################
    # 手机号以110开头的作者出版过的所有书籍名称以及书籍出版社名称
    # 方式1:
    # 需求: 通过Book表join AuthorDetail表, Book与AuthorDetail无关联,所以必需连续跨表
    # ret=Book.objects.filter(authors__authordetail__telephone__startswith="110").values("title","publish__name")
    # print(ret)
    #
    # # 方式2:
    # ret=Author.objects.filter(authordetail__telephone__startswith="110").values("book__title","book__publish__name")
    # print(ret)

    # -------------------------聚合与分组查询---------------------------
    # 查询所有书籍的平均价格
    # Book.objects.all().aggregate(avg_price=Avg('price'))    # aggregate( 变量名 = 函数（‘变量’）)

    # 单表分组查询的ORM语法: 单表模型.objects.values("group by的字段").annotate(聚合函数("统计字段"))
    # 跨表分组查询的ORM语法: 多表模型.objects.values("group by的字段").annotate(聚合函数("关联表__统计字段")).values("表模型的所有字段+统计出来的字段"(可选))
    #                     每一个后的表模型.objects.annotate(聚合函数(关联表__统计字段)).values("表模型的所有字段以及统计字段")

    return HttpResponse('200 OK')


def insertdata_func(request):
    # 批量插入数据库
    book_list = []
    a = 1555772380
    b = 1629772380
    for i in range(100):
        publisher = random.randint(1, 8)    #随机出版社
        rtime = time.localtime(random.randint(a, b))
        rtime = time.strftime('%Y-%m-%d', rtime)
        book = Book(title=f'book{i}', publishDate=rtime, price=i+100, publish_id=publisher)
        book_list.append(book)
    Book.objects.bulk_create(book_list)
    print('成功插入')
    return HttpResponse('插入成功')


@login_required
def main_func(request):
    # print(request.COOKIES)
    # is_login = request.COOKIES.get('is_login')
    # username = request.COOKIES.get('username')
    print(request.user)
    # print("user", request.user.username)
    print("is_anonymous", request.user.is_anonymous)
    usn = request.user.username
    is_anonymous = request.user.is_anonymous

    if not is_anonymous:
        book_list = Book.objects.all()
        # 分页器
        paginator = Paginator(book_list, 8)
        # print(paginator.num_pages, paginator.count, paginator.page_range)
        nums = paginator.num_pages
        cpage = int(request.GET.get('page', 1))  # 娶不到结果的话，默认值为一

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

        return render(request, 'main.html', locals())
    else:
        return render(request, 'login.html')


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
            User.objects.create_user(usn=request.POST.get('usn'),
                                    pwd=request.POST.get('usn'),
                                    email=request.POST.get('email'))


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
        user = auth.authenticate(username=usn, password=pwd)

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

    return render(request, 'login.html', locals())


def logout_func(request):
    '''注销账户'''
    auth.logout(request)
    return redirect('/main/')

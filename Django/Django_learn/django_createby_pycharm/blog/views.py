
# Create your views here.
import datetime

import requests
from django.shortcuts import render, HttpResponse
from django.urls import reverse

def timer(request):
    ctime = datetime.datetime.now().strftime('%Y-%m-%d %X')
    return render(request, 'timer.html', {"ctime": ctime})


def special_case_2000(request):
    url = reverse('blog:ate2000')   # 用于函数内部的反向解析
    print(url)
    return HttpResponse('special_case_2000')

def year_archive(request, year):
    # 用于函数内部的反向解析，当含有正则表达式的时候，用任意一个正则匹配的数字作为参数传入即可，有几个正则，就要传入几个参数
    url = reverse('blog:atexxxx', args=(1234, ))   # 前面‘blog’是命名空间
    print(url)
    return HttpResponse(f'你访问的是{year}年')

def month_archive(request, year, month):
    return HttpResponse(f'你访问的是{year}年{month}月')

def article_detail(request, year, month, day):
    return HttpResponse(f'你访问的是{year}年{month}月{day}日')

def login(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        print(request.POST)
        usn = request.POST.get('usn')
        pwd = request.POST.get('pwd')
        if usn == 'zhougongjin' and pwd == '666':
            return HttpResponse('200 OK')
        else:
            return HttpResponse('用户不存在')


def user_age(request, age):
    print(age)
    return HttpResponse(f'你的年龄是{age}岁')



def month_response(request, month):
    print(month, type(month))
    return HttpResponse(f'现在是{month}月')

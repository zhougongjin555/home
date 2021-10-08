"""django_createby_pycharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog.views import timer, special_case_2000, year_archive, month_archive, article_detail, user_age



urlpatterns = [
    # django1.0 re_path()  正则定义路径  ?P<name> 定义参数的变量名，实现有名分组
    re_path(r'^articles/2000/$', special_case_2000, name='ate2000'),  # 用于函数内部的反向解析
    re_path(r'^articles/(?P<year>[0-9]{4})/$', year_archive, name='atexxxx'),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', article_detail),

    # django path()
    path(r"articles/<int:age>", user_age),

]

''' str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
    int,匹配正整数，包含0。
    slug,匹配字母、数字以及横杠、下划线组成的字符串。
    uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
    path,匹配任何非空字符串，包含了路径分隔符，不能为'？'
'''

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
from django.urls import path, re_path, include, register_converter
from blog.views import timer, login, month_response
from blog.urlconvert import Mon_convert

register_converter(Mon_convert, 'mon_convert')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', timer),   # 自动执行timer(request)，必须要有request参数
    path('login/', login, name='log'),  # name起别名，用于反向解析

    # 分发
    re_path(r'blog/', include(("blog.urls", 'blog'))),      # include(('分发路由地址'， '命名空间'))


    path(r'regex/<mon_convert:month>', month_response)
]

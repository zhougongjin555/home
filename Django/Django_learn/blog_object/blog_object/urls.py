"""blog_object URL Configuration

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
from django.views.static import serve

from blog_object import settings
from blog.views import login_func, upload_func, valid_code_func, main_func, register_func, logout_func, home_func, article_detail_func, updown_func, comment_func, comment_tree_func, manage_func, add_article_func



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_func),
    re_path('^$', main_func),
    path('register/', register_func),
    path('login/', login_func),
    path('valid_code/', valid_code_func),
    path('logout/', logout_func),
    path('updown/', updown_func),
    path('comment/', comment_func),
    path('comment_tree/', comment_tree_func),
    path('upload/', upload_func),
    re_path('manage/$', manage_func),
    re_path('manage/add_article/$', add_article_func),

    # media 配置
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 个人站点URL
    re_path(r'^(?P<username>\w+)$', home_func),

    # 设计页面跳转URL
    re_path(r'^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', home_func),

    # 设计文章内容跳转页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/$', article_detail_func),

]

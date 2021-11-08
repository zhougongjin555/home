"""drftest URL Configuration

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
from drf import views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/user/', views.UserView.as_view()),  # get传递版本信息
    # re_path(r'^api/(?P<version>\w+)/user', views.UserView.as_view()),  #
    # url传递版本信息

    path(r'api/auth/', views.AuthView.as_view()),    # 测试验证
    path(r'api/order/', views.OrderView.as_view()),   # 测试限流
    path(r'api/see/', views.UserGet.as_view()),  # 测试序列化查询

    # 测试五大视图查询
    path('api/views/',
         views.UserViewSite.as_view({"get": "list", "post": "create"})),
    path('api/views//<int:pk>/',
         views.UserViewSite.as_view({"get": "retrieve",
                                     "put": "update",
                                     "patch": "partial_update",
                                     "delete": "destroy"})),

]

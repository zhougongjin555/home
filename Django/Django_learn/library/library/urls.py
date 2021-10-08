"""library URL Configuration

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
from django.urls import path
from book_management.views import add_func, insertdata_func, main_func, register_func, login_func, logout_func, confirm_data, select_func, delete_func, edit_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_func),
    path('insertdata/', insertdata_func),
    path('register/', register_func),
    path('login/', login_func),
    path('logout/', logout_func),
    path('confirm_data/', confirm_data),
    path('select_book/', select_func),
    path('add_book/', add_func),
    path('delete_book/', delete_func),
    path('edit_book/', edit_func),
]

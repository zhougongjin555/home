# coding ：UTF-8
# 开发人员：
# 开发时间： 2021/8/30 16:20
# 文件名称： myforms.py
# 文件地址： blog
# 开发工具： PyCharm
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError

from blog.models import *
class Userform(forms.Form):
    usn = forms.CharField(
        max_length=32,
        label='用户名',
        error_messages={'required': '请填写该内容'},
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'}))
    pwd = forms.CharField(
        max_length=32,
        label='密码',
        error_messages={'required': '请填写该内容'},
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'}))
    pwd1 = forms.CharField(
        max_length=32,
        label='确认密码',
        error_messages={'required': '请填写该内容'},
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'}))
    email = forms.EmailField(
        max_length=32,
        label='邮箱',
        error_messages={'required': '请填写该内容'},
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control'}))

    def clean_usn(self):
        usn = self.cleaned_data.get('usn')
        is_used = UserInfo.objects.filter(username=usn).first()
        if is_used:
            raise ValidationError('用户名已经被使用')
        else:
            return usn


    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        pwd1 = self.cleaned_data.get('pwd1')
        if pwd and pwd1:
            if pwd == pwd1:
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data



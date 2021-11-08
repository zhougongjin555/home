from django.db import models

# Create your models here.

##########################v1
# class UserInfo(models.Model):
#     role_choices = ((1, "普通用户"), (2, "管理员"), (3, "超级管理员"),)
#     role = models.IntegerField(verbose_name="角色", choices=role_choices, default=1)
#
#     username = models.CharField(verbose_name="用户名", max_length=32)
#     password = models.CharField(verbose_name="密码", max_length=64)
#     token = models.CharField(verbose_name="TOKEN", max_length=64, null=True, blank=True)

#############################v2
class Role(models.Model):
    """ 角色表 """
    title = models.CharField(verbose_name="名称", max_length=32)


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name="名称", max_length=32)


class UserInfo(models.Model):
    """ 用户表 """
    level_choices = ((1, "普通会员"), (2, "VIP"), (3, "SVIP"),)
    level = models.IntegerField(verbose_name="级别", choices=level_choices, default=1)

    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄", default=0)
    email = models.CharField(verbose_name="邮箱", max_length=64, default='')
    token = models.CharField(verbose_name="TOKEN", max_length=64, null=True, blank=True)

    # 外键
    depart = models.ForeignKey(verbose_name="部门", to="Department", on_delete=models.CASCADE, default='')

    # 多对多
    roles = models.ManyToManyField(verbose_name="角色", to="Role")


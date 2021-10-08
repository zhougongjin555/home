# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/2 13:20
# 文件名称： my_tags.py
# 文件地址： blog/templatetags
# 开发工具： PyCharm
# 开发功能： 创建自定义的 h5 标签

from django import template
from django.db.models import Count,functions
from blog.models import *


register = template.Library()

# @register.simple_tag   # 装饰函数，可以传入参数

@register.inclusion_tag("classification.html")   # 将返回值传给HTML模板文件
def get_classification_style(username):
    user = UserInfo.objects.filter(username=username).first()
    # 当前的站点对象
    blog = user.blog

    # 每一个分类的文章数，标签的文章数
    category_ret = Category.objects.filter(blog=blog).values('pk').annotate(c=Count("article__title")).values_list(
        'title', 'c')
    # PK代表主键的意思,用于聚合的字段
    tag_ret = Tag.objects.filter(blog=blog).values('pk').annotate(c=Count('article__title')).values_list('title', 'c')

    # 查询每一个年月，以及对应的文章数量
    # 方法1
    time_ret = Article.objects.filter(user=user).extra(
        select={"y_m_date": "date_format(create_time, '%%Y-%%m')"}).values("y_m_date") \
        .annotate(c=Count('pk')).values_list("y_m_date", "c")

    # 方法2
    time_ret2 = Article.objects.filter(user=user).annotate(month=functions.TruncMonth('create_time')).values('month') \
        .annotate(c=Count('pk')).values_list("month", "c")

    return {'blog': blog, 'category_ret': category_ret, 'tag_ret': tag_ret, 'time_ret2': time_ret2, 'username': username}


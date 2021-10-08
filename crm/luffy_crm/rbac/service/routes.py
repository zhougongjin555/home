#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import URLResolver, URLPattern


def check_url_exclude(url):
    """
    排除一些特定的URL
    :param url:
    :return:
    """
    for regex in settings.AUTO_DISCOVER_EXCLUDE:
        if re.match(regex, url):
            return True


def recursion_urls(patterns, pre_url, url_ordered_dict, pre_namespace):
    """
    递归的去获取URL
    :param patterns: 路由关系列表
    :param pre_url: url前缀，以后用于拼接url
    :param url_ordered_dict: 用于保存递归中获取的所有路由
    :param pre_namespace: namespace前缀，以后用户拼接name
    :return:
    """
    for item in patterns:
        if isinstance(item, URLPattern):  # 非路由分发，加入到字典
            if not item.name:  # 如果item.app_name等于None则不递归,提高效率，注意此处必须在url配置namespace
                continue
            if pre_namespace:
                name = f'{pre_namespace}:{item.name}'  # 获取命名空间名
            else:
                name = item.name

            # 拼接  “ / ”  和   ‘URL’，并且替换正则符号
            url = (pre_url + item.pattern.regex.pattern).replace("^", '').replace("$", "")
            if check_url_exclude(url):
                continue
            url_ordered_dict[name] = {'name': name, 'url': url}


        elif isinstance(item, URLResolver):  # 路由分发，递归操作
            if pre_namespace:
                if item.namespace:
                    namespace = f'{pre_namespace}:{item.namespace}'  # 获取命名空间名
                else:
                    namespace = item.namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            recursion_urls(item.url_patterns, pre_url + item.pattern.regex.pattern, url_ordered_dict, namespace)
    return url_ordered_dict


def get_all_url_dict():
    """
    获取项目中所有的URL（必须有name别名）
    :return:
    """
    url_ordered_dict = OrderedDict()

    md = import_string(settings.ROOT_URLCONF)  # from luff.. import urls
    # for item in md.urlpatterns:
    #     print(item)

    recursion_urls(md.urlpatterns, '/', url_ordered_dict, None)  # 递归去获取所有的路由

    return url_ordered_dict

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2021/09/14
# @Author  : 周公瑾
# @File    : AES加密.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-



from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

SALT = ""

IV = ""

def aes_encrypt(data_string):
    key = "asdsfasdasdasdasdasfasfasdasd"
    iv = "asdafasdaas"
    aes = AES.new(
        key=key.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=iv.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)

data = 'asdasdasdasfasdasasdasdasfd'
result = aes_encrypt(data)
print(result)


class Foo(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f1(self):
        print("绑定方法", self.name)

    @classmethod
    def f2(cls):
        print("类方法", cls)

    @staticmethod
    def f3():
        print("静态方法")


# 绑定方法（对象）
obj = Foo("武沛齐", 20)  # 实例化对象
obj.f1()  # Foo.f1(obj)

# 类方法
Foo.f2()  # cls就是当前调用这个方法的类。（类）   主流
obj.f2()  # cls就是当前调用这个方法的对象的类。



def div(li, a):
    low = -1
    high = len(li)
    while low + 1 != high:
        mid = (low + high) >> 1
        if li[mid] < a:
            low = mid
        elif li[mid] == a:
            return mid
        else:
            high = mid

print(div([1,3,4,5,56,68,233], 68))
import random
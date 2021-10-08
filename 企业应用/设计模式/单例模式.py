# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/17 14:49
# 文件名称： 单例模式.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a

a = MyClass(100)
b = MyClass(200)
print(a.a, id(a))
print(b.a, id(b))

# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/16 17:21
# 文件名称： 接口.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能： 抽象方法

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    '''
        加上抽象的方法，要求子类必须按照父类定义的方式 定义 此方法，如果不定义就报错
        并对高层模块隐藏了类的内部实现
        'TypeError: Can't instantiate abstract class Aliapy with abstract methods pay'
    '''
    @abstractmethod
    def pay(self, money):
        pass

class Aliapy(Payment):
    pass

class Wechat(Payment):
    def pay(self, money):
        print(f'微信支付{money}元')

w = Wechat()
a = Aliapy()




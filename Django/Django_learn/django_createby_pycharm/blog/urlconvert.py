'''django2.0 urls 自定义转化器'''
class Mon_convert:
    regex = '[0-9]{2}'

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):  # 反向解析
        pass



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

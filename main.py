import os 
import requests
os.path.exists('F:\predict.csv')
import configparser
#
#
#
# with open("./file/beauty.csv", mode='rt', encoding='utf-8') as f:
#     f.readline()
#     for line in f:
#         url = line.strip().split(',')
#         content = requests.get(url[-1]).content
#
#         # 判断路径是否存在
#         if not os.path.exists("file"):
#             os.mkdir('file')
#
#         name = url[1].replace('/', '')
#         with open(f'./file/{name}.png', mode='wb') as w:
#             w.write(content)
#         print(url)
#


config = configparser.ConfigParser()
config.read('./file/config.ini', encoding='utf-8')

print(config.sections()) # 获取所有的节点
print(config.items('mysqld')) # 获取节点对应的所有值
print(config.get('mysqld', 'datadir')) # 获取节点里面的键对应值


config.has_section('mysqld') # 判断是否有节点
# 增加节点
config.add_section('group')
config.set('group', 'addddd')# 设置键的值
config.write(open('./file/config.ini', mode='r', encoding='utf-8'))

# 删除节点
config.remove_section('group')
config.remove_option('group', 'addddd') # 只删除键的值

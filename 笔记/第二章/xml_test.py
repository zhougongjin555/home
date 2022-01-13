from lxml import etree
from xml.etree import ElementTree as ET

# tree = ET.parse('./file/net.xml')
#
# # 获取根标签
# root = tree.getroot()
# print(root)
#
# countty_obj = tree.find("country") # 找节点
# print(countty_obj.tag, countty_obj.attrib, countty_obj.text) # 找标签，值，文本
#
#
# # 更新标签里面的值
# rank = tree.find('country').find('rank')
# rank.set('update', '2021-07-24')
# rank.text = 'aaa'  #更新标签的文本
# tree.write("./file/net.xml", encoding='utf-8')
#
# # 删除节点
# tree._root.remove(tree.find('country'))
# tree.write("./file/net.xml", encoding='utf-8')






# 创建xml
# 根节点
root = ET.Element('home')

# 子节点
son1 = ET.Element('son', {'name': 'child1'})
son2 = ET.Element('son', {'name': 'child2'})

# 孙节点
grandson1 = ET.Element('grandson', {'name': 'grandchild1'})
grandson2 = ET.Element('grandson', {'name': 'grandchild2'})
# 孙-->子
son1.append(grandson1)
son1.append(grandson2)

# 把儿子添加到根节点中
root.append(son1)
root.append(son2)

tree = ET.ElementTree(root)
tree.write('./file/oooo.xml', encoding='utf-8', short_empty_elements=False)
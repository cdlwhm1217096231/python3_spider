# -*- coding: UTF-8 -*-
import json

"""
JSON文件存储操作
"""
# JSON数据格式由数组和对象组成，对象一般用{}包裹，是键值对结构，数组一般用[],一般是索引结构，也可以采用键值对
# 1、读取JSON数据  ----使用JSON库
# 1.1 loads()方法将ISON文本字符串转化为JSON对象
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print('原始数据类型:', type(str))
data = json.loads(str)
print('将JSON字符串转化为JSON对象:\n', data)
print('转化后的数据类型:', type(data))
print('使用索引得到列表元素方法1', data[0]['name'])
print('使用索引得到列表元素方法2', data[0].get('name'))  # 推荐此方法
print(data[0].get('age'))  # 无age这个键名
# 从JSON文本中读取字符串
filename = 'data.json'
with open(filename, 'r') as f:
    str = f.read()
    data = json.loads(str)
    print(data)
# 1.2 dumps()方法将JSON对象转化为字符串
import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'date': '1992-10-1'
}]
with open('data.json', 'w')as f:
    f.write(json.dumps(data))

# 含有中文情况的处理
info = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('info.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(info, indent=2, ensure_ascii=False))





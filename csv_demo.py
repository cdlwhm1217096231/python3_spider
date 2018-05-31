# -*- coding: UTF-8 -*-
import csv
"""
CSV文件的存储操作
"""
# 1.写入
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# 同时写入多行
with open('data1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['1001', 'Mike', 20], ['1002', 'Bob', 23], ['1003', 'Curry', 21]])

# 以字典的形式写入
with open('data2.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
# 在原有的数据基础上添加数据
with open('data2.csv', 'a', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': 1004, 'name': 'curry', 'age': 234})

# 写入中文字符，解决编码问题
with open('data2.csv', 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': 1004, 'name': '王伟', 'age': 24})

# CSV文件的读取
with open('data2.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)   # 逐行读取

import pandas as pd

# 使用pandas库读取csv文件
df = pd.read_csv('data2.csv')
print('pandas库读取csv文件:\n', df)

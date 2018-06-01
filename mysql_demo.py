#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-01 15:44:48
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pymysql

# 1、连接到数据库
db = pymysql.connect(host='localhost', user='root',
                     password='123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()   # 返回结果中的第一条数据
print('Datebase Version:', data)
# 创建一个名为spiders的数据库
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8")
db.close()

# 2、创建表
import pymysql

# db = pymysql.connect(host='localhost', user='root',
#                      password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name  VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# 3、插入数据
import pymysql

id = '20180003'
user = 'james'
age = 33
db = pymysql.connect(host='localhost', user='root',password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()    # 将数据提交到数据库中，对插入、更新、删除操作都需要该方法
except:
    db.rollback()
db.close()

# 无需改变插入方法，则传入一个动态变化的字典，做成一个通用方法
data = {
    'id': '20180002',
    'name': 'Harden',
    'age': 29
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders' )
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
    table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

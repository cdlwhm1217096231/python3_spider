# -*- coding: UTF-8 -*-
import pymysql

# 3、插入数据基本用法

# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# id = '20120001'
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 插入数据高级用法   构造动态字典，实现通用的插入方法，不用修改插入方法
# data = {
#     'id': '20120002',
#     'name': 'Dad',
#     'age': 10086
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#    if cursor.execute(sql, tuple(data.values())):
#        print('Successful')
#        db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

# 4、更新数据-------基本用法

# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#    cursor.execute(sql, (25, 'Bob'))   # 将年龄修改为25
#    cursor.execute(sql, (35, 'Dad'))   # 将年龄10086修改为35
#    db.commit()
# except:
#    db.rollback()
# db.close()
# 更新数据 ---高级用法（支持灵活的字典传值）
"""
如果数据已经存在，则更新数据，不重复保存；当数据不存在，则插入数据
"""
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120004',
    'name': 'James',
    'age': 22
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
# 5、删除数据
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# condition = 'age > 20'
#
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 6、查询数据 -------基本用法
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')
# 查询数据 ------高级用法（推荐此方法)
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
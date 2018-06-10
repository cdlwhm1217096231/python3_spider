#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-05 22:04:34
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
import pymongo

# 连接mongodb,创建MongoDB的连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 指定要使用的数据库的名字为--- test
db = client.test    # db = client['test']

# 指定集合为students,每个数据库包含多个集合，类似于关系型数据库中的表
collection = db.students   # collection = db['students']
# 插入操作
student = {
    'id': '20180610',
    'name': 'Curry',
    'age': 30,
    'gender': 'male'
}
result = collection.insert(student)  # 调用collection的insert()方法插入数据
print(result)  # mongodb中每一条数据都有一个_id属性来唯一标识，insert()方法返回的是_id的值
# 插入多条数据时，以列表形式传入多条数据，具体见下面的例子
student1 = {
    'id': '20180601',
    'name': 'Harden',
    'age': 28,
    'gender': 'male',
}

student2 = {
    'id': '20180602',
    'name': 'Durant',
    'age': 29,
    'gender': 'male',
}
result = collection.insert([student1, student2])
print(result)
# python3中推荐的插入方法
student = {
    'id': '20180610',
    'name': 'James',
    'age': 33,
    'gender': 'male'
}
result = collection.insert_one(student)
print(result)  # 返回的是InsertOneResult对象，使用inserted_id属性获取_id属性
print(result.inserted_id)
# 插入多条数据
student3 = {
    'id': '2018001',
    'name': 'Paul',
    'age': 33,
    'gender': 'male',
}

student4 = {
    'id': '2018002',
    'name': 'West',
    'age': 36,
    'gender': 'male',
}

result = collection.insert_many([student3, student4])
print(result)
print(result.inserted_ids)
# 查询操作 ---使用find_one()或者find()方法进行查询
result = collection.find_one({'name': 'Curry'})
print(type(result))
print(result)  # 返回字典类型的值
# 使用ObjectId来查询
from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5b1c870a8cdbe319142dea79')})
print(result)  # 结果存在
result = collection.find_one({'_id': ObjectId('5b1c870a8cdbe319142dea7f')})
print(result)  # 结果不存在，返回None
# 多条数据的查询，使用find()
results = collection.find({'age': 33})
print(results)  # 返回的是一个cursor类型的数据，相当于一个生成器
for result in results:
    print(result)
# 添加筛选条件，进行数据筛选,选出小于等于30岁以下的运动员信息
results = collection.find({'age': {'$lte': 30}})
print(results)
for result in results:
    print(result)
# 使用正则匹配进行查询
results = collection.find({'name': {'$regex': '^D.*'}})
print(results)
for result in results:
    print(result)
# 计数 --- 统计查询结果中有多少条数据
result = collection.find().count()
print('总共有%d条数据' % result)
# 添加筛选条件后的数据个数
result = collection.find({'age': {'$lte': 30}}).count()
print('小于等于30岁数据条数有%d' % (result))
# 排序操作
results = collection.find().sort('name', pymongo.ASCENDING)
print('调用ASCENDING进行升序排列:\n', [result['name'] for result in results])

results = collection.find().sort('age', pymongo.DESCENDING)
print('调用DESCENDING进行降序排列:\n', [result['age'] for result in results])
# 偏移 ----只想取某几个元素，利用skip()方法偏移几个位置；偏移2，就忽略前两个元素，得到第三个及以后的元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print('从第三个元素开始，调用ASCENDING进行升序排列:\n', [result['name'] for result in results])
# 使用limit()限定索取的结果个数
results = collection.find().sort('age', pymongo.DESCENDING).limit(6)
print('调用DESCENDING进行降序排列,只取两个元素:\n', [result['age'] for result in results])
# 更新操作
condition = {'name': 'Curry'}  # 查询条件
student = collection.find_one(condition)
student['age'] = 28  # 更新条件
result = collection.update(condition, student)
print(result)
# 使用$set操作符对数据进行更新
condition = {'name': 'Curry'}  # 查询条件
student = collection.find_one(condition)
result = collection.update(condition, {'$set': student})
print(result)
# python3中使用update_one()和update_many()
condition = {'name': 'Harden'}
student = collection.find_one(condition)
student['age'] = 29
result = collection.update_one(condition, {'$set': student})
print(result)
print('获得匹配的数据条数:%d, 影响的数据条数:%d' % (result.matched_count, result.modified_count))
condition = {'age': {'$gt': 30}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print('获得匹配的数据条数:%d, 影响的数据条数:%d' % (result.matched_count, result.modified_count))
condition = {'age': {'$gt': 30}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print('获得匹配的数据条数:%d, 影响的数据条数:%d' % (result.matched_count, result.modified_count))
print('验证结果:')
results = collection.find({'age': {'$gt': 30}})
for result in results:
    print(result)
# 删除操作
result = collection.remove({'name': 'James'})
print(result)
# python3中使用detete_one和delete_many方法删除元素
result = collection.delete_one({'name': 'West'})
print(result)
print('删除数据%d条' % result.deleted_count)
# 同时删除多条数据
result = collection.delete_many({'age': {'$lt': 30}})
print(result)
print('删除数据%d条' % result.deleted_count)

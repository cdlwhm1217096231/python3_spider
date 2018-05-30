#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-30 10:06:21
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 一、初始化
# 1、字符串初始化
from pyquery import PyQuery as pq

html = """
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""
doc = pq(html)  # 字符串初始化pyquery对象
print(doc('li'))  # 选取li节点

# 2、URL初始化
from pyquery import PyQuery as pq

url = 'https://cuiqingcai.com'
doc = pq(url)  # URL初始化
print('选取title节点:', doc('title'))

# 3.文件初始化
from pyquery import PyQuery as pq

doc = pq(filename='html_demo.html')  # 文件初始化，建立文件html_demo.html
print(doc('li'))

# 二、基本CSS选择器

from pyquery import PyQuery as pq

html = """
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""
doc = pq(html)
print('嵌套选择:\n', doc('#container .list li'))
print('数据类型:', type(doc('#container .list li')))
# 三、查找节点

# 1.子节点
from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
print('items数据类型', type(items))
print(items)
lis = items.find('li')  # 查找items节点的所有子孙节点
print('lis数据类型', type(lis))
print(lis)

lis = items.children()  # 查找items节点的所有子节点
print(lis)

lis = items.children('.active')  # 查找items节点的所有子节点，筛选出class为active的节点
print(lis)
# 2、父节点
from pyquery import PyQuery as pq

html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0">first item</li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
"""
doc = pq(html)
items = doc('.list')
container = items.parent()  # 选取class为list节点的直接父节点
print('直接父节点:\n', container)

doc = pq(html)
items = doc('.list')
parents = items.parents()   # 选取class为list节点的祖先节点
print('祖先节点:\n', parents)

doc = pq(html)
items = doc('.list')
parents = items.parents('.wrap')
print('筛选某个祖先节点:\n', parents)
# 3、兄弟节点
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.list .item-0.active')
print('选择兄弟节点:\n', li.siblings())  # 选择li节点的兄弟节点

doc = pq(html)
li = doc('.list .item-0.active')
print('选择某个兄弟节点:', li.siblings('.active'))

# 4、遍历
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print('选择单个节点:', li)

doc = pq(html)
lis = doc('li').items()
for li in lis:
    print('符合条件的，多个节点需要遍历输出:\n', li)

# 5.获取信息
# 5.1 获取属性
from pyquery import PyQuery as pq

doc = pq(html)
a = doc('.item-0.active a')
print('a标签', a)
print('a标签中的某个属性方法1', a.attr('href'))
print('a标签中的某个属性方法2', a.attr.href)

doc = pq(html)
a = doc('a')
print('选择所有的a标签:\n', a)
print(a.attr.href)  # 只返回第一个a节点的属性值
# 下面使用遍历的方法，调用items()方法,获得所有a节点的属性值
doc = pq(html)
a = doc('a')
for item in a.items():
    print(item.attr.href)
# 5.2 获取文本

from pyquery import PyQuery as pq

doc = pq(html)
a = doc('.item-0.active a')
print('获取a标签中的文本值', a.text())

doc = pq(html)
li = doc('.item-0.active')
print('选取li节点', li)
print('获取li节点内部的HTML文本', li.html())

doc = pq(html)
li = doc('li')
# 获得多个节点的结果时，html()方法得到的是第一个节点的返回结果， 可以使用遍历返回每个节点的结果
print('获得多个节点的结果时，html()方法得到的是第一个节点的返回结果', li.html())
print('text()方法得到所有节点的结果', li.text())  # text()方法得到所有节点的结果

doc = pq(html)
li = doc('li')
for item in li.items():
    print('遍历获得每个节点的html文本:\n', item.html())
# 6、节点操作
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print('原li节点:', li)
print('删除class属性:', li.removeClass('active'))
print('添加class属性:', li.addClass('active'))

from pyquery import PyQuery as pq

html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
"""
doc = pq(html)
li = doc('.item-0.active')
print('原li节点:', li)
li.attr('name', 'link')
print('添加属性名是name，属性值是link的属性', li)
li.text('changed item')
print('添加节点内纯文本内容', li)
li.html('<b>changed item</b>')
print('添加节点内HTML文本', li)

from pyquery import PyQuery as pq
html = """
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
"""
doc = pq(html)
wrap = doc('.wrap')
wrap.find('p').remove()
print(wrap.text())

# 7.伪类选择器
html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
"""
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('li:first-child')
print('选择第一个节点', li)
li = doc('li:last-child')
print('选择最后一个节点', li)
li = doc('li:nth-child(2)')
print('选择第二个li节点', li)
li = doc('li:gt(2)')
print('选择第三个li节点之后的所有li节点\n', li)
li = doc('li:nth-child(2n)')
print('选择所有偶数位置的li节点\n', li)
li = doc('li:contains(second)')
print('选择包含second文本的li节点', li)

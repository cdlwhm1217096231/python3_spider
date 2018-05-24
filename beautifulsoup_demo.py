#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  # 补全代码
print(soup.title.string) #  获取文本，用string属性
# 一、节点选择器，速度快，如果单个节点结构话层次非常清晰，可以选用这种方式来解析。
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 选择元素，默认是第一个符合条件的元素
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.p)
print(soup.head)
# 选择名称(利用 name 属性来获取节点的名称)
soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)
# 获取属性（每个节点可能有多个属性，比如 id，class 等等，我们选择到这个节点元素之后，可以调用 attrs 获取所有属性。）
soup = BeautifulSoup(html, 'lxml')
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p.attrs['class'])
# 上面的写法还有点繁琐，还有一种更简单的获取方式，我们可以不用写 attrs，直接节点元素后面加中括号，传入属性名就可以达到属性值了，样例如下：
print(soup.p['name'])
print(soup.p['class'])
# 获取内容 (可以利用 string 属性获取节点元素包含的文本内容)
print(soup.p.string)
# 嵌套选择
html = """
<html><head><title>The Dormouse's story2</title></head>
<body>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
# 关联选择（选取子节点、父节点、兄弟节点）
# 1.子节点与子孙节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
# 选取到了一个节点元素之后，如果想要获取它的直接子节点可以调用 contents 属性
print(soup.p.contents)
# 调用了 children 属性来进行选择，返回结果可以看到是生成器类型，所以接下来我们用 for 循环输出了一下相应的内容，内容其实是一样的，
# 只不过 children 返回的是生成器类型，而 contents 返回的是列表类型
soup = BeautifulSoup(html, 'lxml')
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 要得到所有的子孙节点的话可以调用 descendants 属性,descendants 会递归地查询所有子节点，得到的是所有的子孙节点。
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)
# 2.父节点和祖先节点
# 如果要获取某个节点元素的父节点，可以调用 parent 属性：

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print('a节点的父节点是:\n', soup.a.parent)
# 上面仅仅是 a 节点的直接父节点，而没有再向外寻找父节点的祖先节点，如果我们要想获取所有的祖先节点，可以调用 parents 属性：
# 列表输出了它的索引和内容，可以发现列表中的元素就是 a 节点的祖先节点。
soup = BeautifulSoup(html, 'lxml')
print(type(soup.a.parents))
print('a节点的所有父节点:\n', list(enumerate(soup.a.parents)))
# 3、兄弟节点
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print('下一个兄弟节点:', soup.a.next_sibling)
print('上一个兄弟节点:', soup.a.previous_sibling)
print('前面所有的兄弟节点:', list(enumerate(soup.a.next_siblings)))
print('后面所有的兄弟节点:', list(enumerate(soup.a.previous_siblings)))
# 提取信息
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print('获取直接子节点的文本:', soup.a.next_sibling.string)
print('获取第一个父节点:\n', list(soup.a.parents)[0])
print('获取父节点的属性:', list(soup.a.parents)[0].attrs['class'])
# 二、方法选择器(find_all() 和 find() )
# 根据节点名查询元素
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print('查询所有节点名是ul的节点:\n', soup.find_all(name='ul'))
print('第一个ul节点的类型:', type(soup.find_all(name='ul')[0]))
# 嵌套查询；查询ul节点内部的li节点
for ul in soup.find_all(name='ul'):
    print('嵌套选择结果:', ul.find_all(name='li'))
# 嵌套选择li节点的文本
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print('文本值是:\n', li.string)
# 除了根据节点名查询，我们也可以传入一些属性来进行查询
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print('选择属性方法1:\n', soup.find_all(attrs={'id': 'list-1'}))
print('选择属性方法1:\n', soup.find_all(attrs={'name': 'elements'}))
# 对于一些常用的属性比如 id、class 等，我们可以不用 attrs 来传递，比如我们要查询 id 为 list-1 的节点，我们可以直接传入 id 这个参数
print('选择属性方法2:\n', soup.find_all(id='list-1'))
print('选择属性方法2:\n', soup.find_all(class_='element'))  # 注意此处的class应该避免与关键字class同名
# text 参数可以用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print('用text加正则表达式获取文本:', soup.find_all(text=re.compile('link')))
#  find()
# 除了 find_all() 方法，还有 find() 方法，只不过 find() 方法返回的是单个元素，也就是第一个匹配的元素，而 find_all() 返回的是所有匹配的元素组成的列表。
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list list-small'))
'''
find_parents() 返回所有祖先节点，find_parent() 返回直接父节点。
find_next_siblings() 返回后面所有兄弟节点，find_next_sibling() 返回后面第一个兄弟节点。
find_previous_siblings() 返回前面所有兄弟节点，find_previous_sibling() 返回前面第一个兄弟节点。
find_all_next() 返回节点后所有符合条件的节点, find_next() 返回第一个符合条件的节点。
find_all_previous() 返回节点后所有符合条件的节点, find_previous() 返回第一个符合条件的节点
'''
# 方法三、CSS选择器
# 使用 CSS 选择器，只需要调用 select() 方法，传入相应的 CSS 选择器即可
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print('css嵌套选择:\n', soup.select('.panel .panel-heading'))
print('ul节点下嵌套li节点:\n', soup.select('ul li'))
print('id属性下的class属性:\n', soup.select('#list-2 .element'))
print('判断ul节点的类型', type(soup.select('ul')[0]))
# 嵌套选择
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    for li in ul.select('li'):
        print(li.get_text())
# 获取属性
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print('方法1:', ul['id'])
    print('方法2:', ul.attrs['id'])
# 获取文本
#  get_text()，同样可以获取文本值。
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('方法1:', li.get_text())
    print('方法2:', li.string)
# 总结
'''
推荐使用 LXML 解析库，必要时使用 html.parser。
节点选择筛选功能弱但是速度快。
建议使用 find()、find_all() 查询匹配单个结果或者多个结果。
如果对 CSS 选择器熟悉的话可以使用 select() 选择法。
'''









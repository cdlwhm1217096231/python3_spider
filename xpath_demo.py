#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
解析库lxml中xpath方法的使用
'''
from lxml import etree
# 1.XPath方法常用规则
'''
nodename  选取此节点的所有子节点
/         从当前节点选取直接子节点
//        从当前节点选取所有子孙节点
.         选取当前节点
..        选取当前节点的父节点
@         选取属性
'''
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)  # 输出修正后的HTML代码
print(result.decode('utf-8'))
# 直接读取文件test.html进行解析
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print('直接读取html文件进行解析：\n', result.decode('utf-8'))
# 2.所有节点
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')  # *代表匹配所有节点
print('匹配所有节点:\n', result)  # 返回列表类型

# 提取指定的节点名称
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')  # 指定节点名称
print('提取指定的节点li：\n', result)
print(result[0])
# 3.子节点
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a') # 用//作为xpath的开头，/表示提取当前节点的直接子节点
print('选取li节点的直接子节点a:\n', result)

from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul//a') # //a：选取ul节点的所有子孙节点a
print('选取所有的子孙节点a:\n', result)

# 4.父节点
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print('获取父节点:\n', result)

# 5.属性匹配,进行过滤
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print('选取class为item0的li节点:\n', result)
# 6.文本获取
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print('获取文本内容方法1:\n', result)

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print('获取文本内容方法2:\n', result)
# 7.属性获取
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print('获取属性href\t', result)
# 8.属性多值匹配
from lxml import etree

html = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(html)
result = html.xpath('//li[contains(@class, "li")]/a/text()')  # 属性class有两个属性值li li-first
print('属性多值匹配\t', result)
# 9.多属性匹配
html = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(html)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')  # 多个属性确定一个节点，同时匹配多个属性
print("多属性匹配:\n", result)

# 10.按序选择
html = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(html)
result = html.xpath('//li[1]/a/text()')
print('获取第一个li节点的文本\t', result)
result = html.xpath('//li[last()]/a/text()')
print('获取最后一个li节点的文本\t', result)
result = html.xpath('//li[position() < 3]/a/text()')
print('获取位置小于3的li节点文本\t', result)
result = html.xpath('//li[last() -2]/a/text()')
print('获取倒数第3个li节点的文本\t', result)
# 11、节点轴选择
from lxml import etree
html = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(html)
result = html.xpath('//li[1]/ancestor::*')
print('第一个li节点的所有祖先节点\t', result)
result = html.xpath('//li[1]/ancestor::div')
print('第一个li节点的div这个祖先节点\t', result)
result = html.xpath('//li[1]/attribute::*')
print('获取第一个li节点的所有属性值\t', result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print('获取第一个li节点的所有直接子节点的属性为link1.html的a节点\t', result)
result = html.xpath('//li[1]/descendant::span')
print('获取第一个li节点的所有子孙节点中的span节点\t', result)
result = html.xpath('//li[1]/following::*[2]')
print('获取第一个li节点之后的所有节点*,*[2]表示选择当前节点之后的第二个节点:\n', result)
result = html.xpath('//li[1]/following-sibling::*')
print('获取第一个li节点之后的所有同级节点:\n', result)








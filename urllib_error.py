#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request, error
'''
利用urllib库进行异常处理
'''
# URLError是error异常模块的基类
try:
    url = 'https://cuiqingcai.com/index.htm'
    response = request.urlopen(url)
except error.URLError as e:
    print(e.reason)
# HTTPError
# HTTPError是URLError的子类，专门处理HTTP请求错误，有3个属性code、resason、headers
from urllib import request, error
try:
    url = 'https://cuiqingcai.com/index.htm'
    response = request.urlopen(url)
except error.HTTPError as e:
    print(e.code, e.reason, e.headers, sep='\n')

# URLError是HTTPError的父类，可以先捕捉子类的错误，再捕捉父类的错误
from urllib import request, error, parse
try:
    url = 'https://cuiqingcai.com/index.htm'
    response = request.urlopen(url)
except error.HTTPError as e:
    print(e.code, e.reason, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully")
# reason属性有时返回的不一定是字符串，也可以是一个对象
import socket
from urllib import request, error

try:
    url = 'https://www.baidu.com'
    response = request.urlopen(url, timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
# 解析链接用urlparse()方法的基本用法(URL由6部分组成)
from urllib import parse
result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
# urlparse（）方法的高级用法，传入urlstring（必选参数即基本用法中的URL）、scheme、allow_fragments三个参数
# scheme参数是用在URL中不包含协议时使用
url = 'www.baidu.com/index.html;user?id=5#comment'
result = parse.urlparse(url, scheme='https')
print('不带协议参数的结果：', result)
# allow_fragments参数是否忽略fragment
url = 'www.baidu.com/index.html;user?id=5#comment'
result = parse.urlparse(url, scheme='https', allow_fragments=False)
print('忽略fragment参数的结果：', result)
# 当URL中不包含params和query部分时，fragment会被解析为path的一部分
url= 'http://www.baidu.com/index.html#comment'
result = parse.urlparse(url, allow_fragments=False)
# sep='\n'表示当输入多个打印的值时，各个值之间分割方式， 默认空格
# 返回值是一个元组，可以用元素索引或者属性名获取
print(result)
print(result.scheme, result.netloc, sep='\n')
print(result[0], result[1], sep='\n')
# urlunparse()方法的data必须长度为6,实现URL的构造
from urllib import parse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(parse.urlunparse(data))
# urlsplit()方法与urlparse（）方法相似，但不单独解析params这个部分
from urllib import parse
result = parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[1], sep='\n')
# urlunsplit()方法与urlunparse()方法类似，将链接的各个部分组合成完整的链接，传入的data必须长度是5
from urllib import parse
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(parse.urlunsplit(data))
# urljoin()方法，提供两个参数，一个是base_url,一个是新链接。
# 新链接不存在，base_url会提供三项内容协议、域名、路径进行补充；新链接存在，就使用新链接的部分
from urllib import parse
result = parse.urljoin('http://www.baidu.com', 'FAQ.html')
print(result)
result = parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html')
print(result)
# urlencode()方法在构造GET请求时有用
from urllib import parse, robotparser
params = {
    'name': 'curry',
    'age': 30
}
base_url = 'http://www.baidu.com?'
url = base_url + parse.urlencode(params)
print(url)
# Robots协议
from urllib import robotparser
rp = robotparser.RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
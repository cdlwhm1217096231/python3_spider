#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from urllib.error import URLError
import socket
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.request import ProxyHandler, build_opener
import http.cookiejar


url = 'https://www.baidu.com/'
response = urllib.request.urlopen(url)
print(type(response))
print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# 传入data参数
url = 'http://httpbin.org/post'
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')
response = urllib.request.urlopen(url, data=data)
print(response.read())

# 传入timeout参数
url = 'http://httpbin.org/get'
response = urllib.request.urlopen(url, timeout=10)
print(response.read())

# 处理服务器响应超时异常
url = 'http://httpbin.org/get'
try:
    response = urllib.request.urlopen(url, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 利用 urlopen() 方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一个完整的请求
# 如果请求中需要加入 Headers 等信息，我们就可以利用更强大的 Request 类来构建一个请求
url = 'https://www.baidu.com'
# urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个 url 参数是请求 URL，这个是必传参数，其他的都是可选参数
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
form = {
    'name': 'curry',
    'age': 30
}
data = bytes(urllib.parse.urlencode(form), encoding='utf8')
r = urllib.request.Request(url, data=data, headers=headers, method='POST')
# headers 也可以用 add_header() 方法来添加
# re = urllib.request.Request(url, data=data, method='POST')
# re.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = urllib.request.urlopen(re)
# print(response.read().decode('utf-8'))
response = urllib.request.urlopen(r)
print(response.read().decode('utf-8'))

# urllib高级用法Handler Opener 两者关系：利用 Handler 来构建 Opener
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

# 代理
# 添加代理，在此本地搭建了一个代理，运行在 9743 端口上
from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

#  Cookies Cookies 的处理就需要 Cookies 相关的 Handler 了
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)
# 将输出的cookies保存成文本（2种方法）

# 1.使用MozillaCookieJar
filename = 'cookies1.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
# 2.使用 LWPCookieJar
filename = 'cookies2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 将保存为本地的cookies读取出来(2中方法）
# 1.使用 LWPCookieJar
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
# 2.使用MozillaCookieJar
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies1.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
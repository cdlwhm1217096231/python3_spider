#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from bs4 import BeautifulSoup
from urllib import request, parse, error
# 加异常处理模块
try:
    url = 'http://sports.sina.com.cn/nba/'
    response = requests.get(url, timeout=0.1)
    response.encoding = 'utf-8'  # 防止requests得到的文本值乱码
    html = response.text
    print('requests请求库请求的结果:\n', html)
    print('状态码', response.status_code)
except ReadTimeout:
    print('TIME OUT')

# 加异常处理模块
try:
    url = 'http://sports.sina.com.cn/nba/'
    result = request.urlopen(url)
    print('urllib请求库的结果:\n', result.read().decode('utf-8'))
except error.URLError as e:
    print(e.reason)
print('状态码:', result.status)

# 下面是解析部分程序
soup = BeautifulSoup(html, 'lxml')
for p in soup.select('.list .item p'):
    for a in p.select('a'):
        print(a.get_text())
print('----------------------------------这是分隔线-------------------------------------')
for li in soup.select('ul .item'):
    for a in li.select('a'):
        print(a.get_text())



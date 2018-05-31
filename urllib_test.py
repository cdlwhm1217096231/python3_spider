#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 10:01:28
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from urllib import request
from bs4 import BeautifulSoup

# 静态网页数据的爬取
url = 'http://jr.jd.com/'
req = request.Request(url)
response = request.urlopen(req)
html = response.read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('a', 'nav-item-primary')
for item in items:
    print(item.get_text())
print('---------------------------这是分割线----------------------')


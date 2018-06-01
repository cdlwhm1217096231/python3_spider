#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-01 19:54:28
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import io
import sys
import requests
from pyquery import PyQuery as pq

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='gb18030')  # 仅在sublime_text下需要加入
url = 'http://gs.njust.edu.cn/'
req = requests.get(url)
req.encoding = 'utf-8'
html = req.text
# print(html)

doc = pq(html)
items = doc('.fields.pr_fields .Article_Title').items()
print('新闻及链接信息:')
for item in items:
    news = item.find('a').text()
    a = item.find('a')
    print("新闻: " + str(news), "链接: " + str(a.attr.href))

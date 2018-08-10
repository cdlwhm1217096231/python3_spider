#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 13:52:12
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
文件存储
"""
# 1、TXT文本存储1
from pyquery import PyQuery as pq
import requests


url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
html = req.text
print(html)
doc = pq(html)
items = doc('.explore-tab .explore-feed.feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link').text()
    answer = pq(item.find('.content').html()).text()
    filename = 'zhihutxt'
    with open(filename, 'w', encoding='utf-8') as f:
        str = '\n'
        sequence = (question, author, answer)
        f.write(str.join(sequence))
        f.write('\n' + '=' * 50 + '\n')

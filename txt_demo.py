#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 13:52:12
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
文件存储
"""
# 1、TXT文本存储
from pyquery import PyQuery as pq
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='gb18030')  # 仅在sublime_txt下需要加入
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
html = req.text
# print(html)
doc = pq(html)
items = doc('.explore-tab .explore-feed.feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'w', encoding='utf-8')
    str = '\n'
    file.write(str.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

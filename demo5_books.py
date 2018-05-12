#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from requests.exceptions import RequestException
import re
import time

# 获得请求
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析网页
def parse_one_page(html):
    pattern = re.compile('<div.*?hd">.*?pos">(.*?)</span>.*?<div.*?post">.*?href="(.*?)".*?_blank">.*?<div.*?title">.*?_blank">(.*?)</a>.*?<div.*?rating">.*?<span.*?rating_nums">(.*?)</span>.*?<div.*?abstract">(.*?)<br />(.*?)<br />(.*?)</div>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0].strip(),
            'url': item[1].strip(),
            'title': item[2].strip(),
            'rating': item[3].strip(),
            'author': item[4].strip(),
            'publisher': item[5].strip(),
            'date': item[6].strip()
        }


def write_to_file(content):
    with open('result_book.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(start):
    url = 'https://www.douban.com/doulist/1264675/?start=' + str(start)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(20):
        main(start=i * 25)
        time.sleep(1)



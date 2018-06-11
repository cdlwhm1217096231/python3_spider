# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import requests
from urllib.parse import urlencode
import pymongo

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers={
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.weibo
collection = db.weibos
max_page = 20


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page,
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json,page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['微博正文'] = pq(item.get('text')).text()
                weibo['点赞数'] = item.get('attitudes_count')
                weibo['评论数'] = item.get('comments_count')
                weibo['转发数'] = item.get('reposts_count')
                yield weibo


def save_to_mongodb(result):
    if collection.insert(result):
        print('Save to MongoDB')


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongodb(result)


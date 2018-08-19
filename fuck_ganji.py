#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 09:06:49
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import requests
from lxml import etree
from requests.exceptions import RequestException
import multiprocessing
import time
import json
from tqdm import tqdm

"""
修改作者源程序，将请求头中加入cookies参数，同时设置请求延时，防止网站反爬虫；将最后结果保存到本地文件中。最后，导入tqdm模块,利用进度条实时观察程序进度
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie': 'statistics_clientid=me; ganji_xuuid=7596d954-199c-4c3c-d952-25fca2ddb581.1534593378536; gj_footprint=%5B%5B%22%5Cu4e8c%5Cu624b%5Cu623f%5Cu51fa%5Cu552e%22%2C%22http%3A%5C%2F%5C%2Fnj.ganji.com%5C%2Ffang5%5C%2F%22%5D%5D; ganji_uuid=2907488178233947827988; lg=1; xxzl_deviceid=zUzKLYQ20Nt%2Fo0lqCefvg3ZD75UCLBeD%2F7L2UH%2F9H0F0iByxldUp1DE4O5xbkwy3; ershoufangABTest=B; citydomain=nj; __utma=32156897.451111294.1534593386.1534640918.1534642960.4; __utmz=32156897.1534642960.4.4.utmcsr=nj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A35438742886%7D; GANJISESSID=vfo6an3viki0eavbtuqk3s9eqs; __utmc=32156897; xzfzqtoken=lwB1rkUCV%2B4%2BwfpUD38d8cd94gQ2kKUQiDlvqFJSVttMdxz4MmqTu8hkLOPHlLdbin35brBb%2F%2FeSODvMgkQULA%3D%3D; ganji_login_act=1534643470170; __utmb=32156897.6.10.1534642960',
}


def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    try:
        selector = etree.HTML(html)
        ALL = selector.xpath(
            '//*[@id="f_mew_list"]/div[6]/div[1]/div[3]/div[1]/div')
        for div in ALL:
            yield {
                'Title': div.xpath('dl/dd[1]/a/text()')[0],
                'Type': div.xpath('dl/dd[2]/span[1]/text()')[0],
                'Area': div.xpath('dl/dd[2]/span[3]/text()')[0],
                'Towards': div.xpath('dl/dd[2]/span[5]/text()')[0],
                'Floor': div.xpath('dl/dd[2]/span[7]/text()')[0].strip().replace('\n', ""),
                'Decorate': div.xpath('dl/dd[2]/span[9]/text()')[0],
                # 地址需要特殊处理一下
                'Address': div.xpath('dl/dd[3]//text()')[1] + div.xpath('dl/dd[3]//text()')[3].replace('\n', '') + div.xpath('dl/dd[3]//text()')[4].strip(),
                'TotalPrice': div.xpath('dl/dd[5]/div[1]/span[1]/text()')[0] + div.xpath('dl/dd[5]/div[1]/span[2]/text()')[0],
                'Price': div.xpath('dl/dd[5]/div[2]/text()')[0]
            }
        if div['Name', 'Type', 'Area', 'Towards', 'Floor', 'Decorate', 'Address', 'TotalPrice', 'Price'] == None:  # 这里加上判断，如果其中一个元素为空，则输出None
            return None
    except Exception:
        return None


def write_to_file(content):
    with open('result_room', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    for i in tqdm(range(1, 101)):  # 这里设置爬取500页数据，在数据范围内，大家可以自设置爬取的量
        url = 'http://nj.ganji.com/fang5/o{}/'.format(i)
        content = get_one_page(url)
        print('第{}页抓取完毕'.format(i))
        for div in parse_one_page(content):
            # print(div)
            write_to_file(div)
        time.sleep(5)


if __name__ == '__main__':
    main()

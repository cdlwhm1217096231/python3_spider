#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 19:42:20
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo

browser = webdriver.Chrome()
wait = WebDriverWait(browser, timeout=10)
KEYWORD = "iphone"


# 获取商品的列表
def index_page(page):
    print("正在爬取第%d页......" % page)
    try:
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager div.form > input")))
            submit = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#mainsrp-pager div.form > span.btn.J_Submit")))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager li.item.active > span"), str(page)))
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".m-itemlist .items .item")))
        get_products()
    except TimeoutException:
        index_page(page)


# 解析商品列表
from pyquery import PyQuery as pq


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {
            "image": item.find(".pic .img").attr("data-src"),
            "price": item.find(".price").text(),
            "deal": item.find(".deal-cnt").text(),
            "title": item.find(".title").text(),
            "shop": item.find(".shop").text(),
            "location": item.find(".location").text(),
        }
    print(product)
    save_to_mongo(product)


# 保存到MongoDB
MONGO_URL = "localhost"
MONGO_DB = "taobao"
MONGO_COLLECTION = "products"
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print("保存到MongoDB成功!")
    except Exception:
        print("保存到MongoDB失败!")


# 遍历每一页
MAX_PAGE = 100


def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    main()

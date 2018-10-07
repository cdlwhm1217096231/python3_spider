#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-21 13:21:16
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
"""
selenium的使用
"""
# 1. 基本使用
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    html=browser.page_source
    soup=BeautifulSoup(html,"lxml")
    print soup.prettify()
    input = browser.find_element_by_id('kw')
    input.send_keys('python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    print('当前的URL:\n', browser.current_url)
    print('当前的cookies:\n', browser.get_cookies())
    print('网页源代码:\n', browser.page_source)
finally:
    browser.close()
# 2.访问页面
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print('淘宝网网页源代码:\n', browser.page_source)
browser.close()
# 3.查找节点 ----通过查找节点来获取想要的节点，再驱动浏览器完成各种模拟点击、填充表单等操作
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# input1 ----input3三种方法均可以查找单个节点
input1 = browser.find_element_by_id('q')
print('input1', input1)
input2 = browser.find_element_by_css_selector('#q')
print('input2', input2)
input3 = browser.find_element_by_xpath('//*[@id="q"]')
print('input3', input3)
browser.close()
# 通用方法查找单个节点
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input4 = browser.find_element(By.ID, 'q')
print('input4', input)
input5 = browser.find_element(By.NAME, 'q')
print('input5', input)
browser.close()
# 4.查找多个节点---- 返回列表数据类型
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')  # css选择器
print('lis', lis)
browser.close()
# 通用方法查找多个节点
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis1 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print('lis1', lis1)
browser.close()
# 5.节点交互
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')  # 输入文字的方法
time.sleep(10)
input.clear()    # 清除文字的方法
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()  # 点击按钮的方法

# 6.动作链 ----鼠标拖拽、键盘按键等操作没有特定的执行对象，这些动作用动作链来执行
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

# 7.执行javaScript ---- 对某些操作，selenium的API没有提供，此时调用execute_script()方法即可实现
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')   # 将进度条下拉到最底部，然后弹出alert提示
browser.execute_script('alert("To Bottom")')
# 8.获取节点信息

# 获取属性
url = 'https://www.zhihu.com/explore'
browser = webdriver.Chrome()
browser.get(url)
logo = browser.find_element_by_class_name('zu-top-link-logo') # 先选择logo这个节点
print('logo', logo)
print(logo.get_attribute('id'))  # 获取id属性
# 获取文本值
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_class_name('js-signup-noauth')
print('logo', logo.text)
logo1 = browser.find_element_by_css_selector('.zu-top-nav-link')
print('logo1', logo1.text)
# 获取id、位置、标签名、大小
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
question = browser.find_element_by_class_name('zu-top-add-question')
print(question.id)
print(question.location)
print(question.tag_name)
print(question.size)
# 9.切换Frame

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_css_selector('.navbar-header.logo')
print('logo', logo)
print(logo.text)
"""另一种方法"""
logo1 = browser.find_element_by_class_name('logo')
print('logo1', logo1)
print(logo1.text)
# 10.延时等待

# 隐式等待:当查找节点而节点未找到时，将隐式等待一段时间。当超过设定等待时间后，将会抛出异常

from selenium import webdriver

url = 'https://www.zhihu.com/explore'
browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 隐式等待10s
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print('input', input)

# 显式等待 ----指定要查找的节点，指定一个最长等待时间。如果在最长等待时间内加载出来这个节点，就返回查找的节点，否则超时抛出异常

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
print('input:', input)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print('button:', button)
# 11.前进和后退
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com/')
browser.get('https://www.zhihu.com/explore')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

# 12.cookies
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print('当前的cookies:', browser.get_cookies())
browser.add_cookie({'name': 'curry', 'domain': 'www.zhihu.com', 'value': '30'})
print('添加cookies:', browser.get_cookies())
browser.delete_all_cookies()
print('删除所有的cookies:', browser.get_cookies())
browser.close()
# 13.选项卡管理

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print('返回选项卡的代号列表:\n', browser.window_handles)  # 调用window_handles属性获取当前开启的所有选项卡，返回选项卡的代号列表
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.zhihu.com/explore')
# 14.异常处理

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('TIME OUT')
try:
    input = browser.find_element_by_class_name('hello')
    print(input)
except NoSuchElementException:
    print('NO Element')
finally:
    browser.close()

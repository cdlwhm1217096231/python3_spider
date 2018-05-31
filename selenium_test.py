# -*- coding:UTF-8 -*-
from urllib import request
import requests
from selenium import webdriver
import csv  # 存储歌单信息的csv文件
"""
动态网页：
所谓的动态网页，是指跟静态网页相对的一种网页编程技术。
静态网页，随着html代码的生成，页面的内容和显示效果就基本上不会发生变化了——除非你修改页面代码。
而动态网页则不然，页面代码虽然没有变，但是显示的内容却是可以随着时间、环境或者数据库操作的结果而发生改变的。

注意:
值得强调的是，不要将动态网页和页面内容是否有动感混为一谈。
这里说的动态网页，与网页上的各种动画、滚动字幕等视觉上的动态效果没有直接关系.
动态网页也可以是纯文字内容的，也可以是包含各种动画的内容，这些只是网页具体内容的表现形式，无论网页是否具有动态效果
只要是采用了动态网站技术生成的网页都可以称为动态网页。
Selenium库:
使用selenium库解决动态网页问题，Selenium 自己不带浏览器，它需要与第三方浏览器结合在一起使用
虽然这样可以看得更清楚，但不适用于我们的爬虫程序，爬一页就打开一页效率太低，所以我们用一个叫PhantomJS的工具代替真实的浏览器。
PhantomJS库：
是一个“无头”（headless）浏览器。它会把网站加载到内存并执行页面上的JavaScript，但是它不会向用户展示网页的图形界面。
把Selenium和PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，可以处理cookie、JavaScript、header，以及任何你需要做的事情。
PhantomJS并不是python的第三方库，不能用pip安装，到官网下载再把可执行文件拷贝到Python安装目录的Scripts文件夹
"""

url ='http://music.163.com/#/discover/playlist'  # 此链接就是动态网页
req = request.Request(url)
response = request.urlopen(req)
html = response.read().decode('utf-8')
print('使用urllib请求得到的结果:\n', html)
# req = requests.get(url)
# html = req.text
# print('使用requests请求得到的结果:\n', html)
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
driver = webdriver.Chrome()
song_list = open('playlist.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(song_list)
writer.writerow(['标题', '播放量', '链接'])
while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame('contentFrame')
    data = driver.find_element_by_id('m-pl-container').\
        find_elements_by_tag_name('li')
    for i in range(len(data)):
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 50:     # 播放量大于50万的歌单
            msk = data[i].find_element_by_css_selector('a.msk')
            writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
    url = driver.find_element_by_css_selector('a.zbtn.znxt').\
        get_attribute('href')
song_list.close()
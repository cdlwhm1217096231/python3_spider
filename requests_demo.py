# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
'''
请求库requests的使用
'''
# 引入
url = 'https://www.baidu.com/'
# 使用get（）方法，实现一个get请求
result = requests.get(url)
print('result的类型是:\t', type(result))
print('响应状态码是:\t', result.status_code)
print('响应体的内容:\n', result.text)  # str类型，是JSON格式的
print('响应体的类型是:\t', type(result.text))
print('cookies是:\t', result.cookies)
# 使用post（）方法实现一个post请求
url = 'http://httpbin.org/post'
result = requests.post(url)
print(result.text)
# 1、利用requests库构建一个GET请求
import requests
url = 'http://httpbin.org/get'
result = requests.get(url)
print(result.text)
# 对get请求，传入额外参数,参数以字典形式存储
import requests
url = 'http://httpbin.org/get'
data = {
    'name': 'curry',
    'age': 30
}
result = requests.get(url, params=data)
print(result.text)
# result.text是str类型的数据，格式是json格式，如果直接解析返回结果，得到一个字典格式，可以直接调用json（）方法
result = requests.get(url)
print(type(result.text))
print(result.json())
print(type(result.json()))
# 抓取网页
import requests
import re

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2880.4 Safari/537.36'
}
url = 'https://www.zhihu.com/explore'
html = requests.get(url, headers=headers)
print(html.text)
pattern = re.compile('h2.*?question_link.*?Title">(.*?)</a>.*?', re.S)
titles = re.findall(pattern, html.text)
print(titles)
# 抓取二进制数据
url = 'https://github.com/favicon.ico'
html = requests.get(url)
with open('favicon.ico', 'wb') as f:
    f.write(html.content)
# 添加headers
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2880.4 Safari/537.36'
}
url = 'https://www.zhihu.com/explore'
html = requests.get(url, headers=headers)
print(html.text)
# 2.POST请求传递参数
url = 'http://httpbin.org/post'
data = {
    'name': 'curry',
    'age': 30
}
html = requests.post(url, data=data)
print(html.text)
# 高级用法
# 1.文件上传
import requests

url = 'http://httpbin.org/post'
files = {'file': open('favicon.ico', 'rb')}
html = requests.post(url, files=files)
print(html.text)
# 2.cookies
import requests

url = 'https://www.baidu.com'
html = requests.get(url)
print('cookies的内容是:\t', html.cookies)
for key, value in html.cookies.items():
    print(key + ' = ' + value)
# 3.利用cookies维持登录状态
url = 'https://www.zhihu.com'
headers = {
   'Cookie': 'd_c0="AHAuF01gig2PTmuOo8O9i0X746eM_T27pTk=|1525404567"; q_c1=bc62a875e9e14734bf5bf3ccad799ce2|1525404570000|1525404570000; _zap=c569faf1-ff9a-4267-982f-e71552ece0df; l_cap_id="ZmM4NWNjNmRlNTRhNDYzOThhMTI4ZTA5MjQwNjcyMWY=|1526521331|6fb2034094d743dbeb37ee06ad67ef06f511928b"; r_cap_id="MmU4YjBhOGNlMzMwNDU2YWFiN2ViYTEzYmYzNDFhOTE=|1526521331|50a3b7beab42b100f2f0d9c484b0305dcb151a5c"; cap_id="ZWI2OTM0MDNmNWE3NDA0YmE0YzRlYjk4ODUzZjgzMzk=|1526521331|91741b7095a8baa03b33eb4dfbc2c5287305d615"; capsion_ticket="2|1:0|10:1526521602|14:capsion_ticket|44:NDFjMjM0NmFmNWYyNGNmM2EwOTY3YzgxZmEzNmYwODc=|26c5a836dd23d2bd20f0ad6f59be53ccd2944e7255077328dc5190bc5f9a476d"; z_c0="2|1:0|10:1526521641|4:z_c0|92:Mi4xLWdiQkJRQUFBQUFBY0M0WFRXQ0tEU1lBQUFCZ0FsVk5LUzNxV3dDSW9tX3JtSkk5RUl0R25sdXc5YjRIZjdMMFFn|e70ce4ce7edfb94eedb9963586f9e147d7b5638206b603926354e3b0484869a7"; __utma=51854390.598950559.1526520640.1526520640.1526520991.2; __utmz=51854390.1526520991.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20170820=1^3=entry_date=20170820=1; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; _xsrf=d3e8a2c6-97af-41dd-ba3a-f1e2907ee91a',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2880.4 Safari/537.36',
}
html = requests.get(url, headers=headers)
print(html.text)
# 4.会话维持Session()
import requests

url = 'http://httpbin.org/cookies/set/number/123456789'
s = requests.Session()
s.get(url)   # 第一次请求，模拟登录
r = s.get('http://httpbin.org/cookies')  # 会话维持：第二次请求，登录成功后进行下一步操作
print(r.text)
# 5.SSL证书验证
import requests
url = 'https://www.12306.cn'
html = requests.get(url, verify=False) # verify=False就不会报SSLError的错误,但会报警告
print(html.status_code)

# 除去警告信息
import requests
import logging

url = 'https://www.12306.cn'
logging.captureWarnings(True)
html = requests.get(url, verify=False)
print(html.status_code)
# 6.代理设置
'''
import requests

url = 'https://www.taobao.com'
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
    }
requests.get(url, proxies=proxies)
'''
#  7.超时设置
import requests

url = 'https://www.taobao.com'
html= requests.get(url, timeout=1)
print(html.status_code)

# 8.身份验证
'''
import requests

url = 'http://localhost:5000'
html = requests.get(url, auth=('username', 'password'))
print(html.status_code)

'''

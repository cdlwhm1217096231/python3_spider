#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/26 17:05'
__author__ = 'cdl'

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 过滤字符串只保留中文
def translate(str):
    line = str.strip()
    p2 = re.compile('[^\u4e00-\u9fa5]')   #中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    zh = ",".join(zh.split())
    str = re.sub("[A-Za-z0-9!！，%\[\],。]", "", zh)
    return str

def word_cloud(csv_file, stopwords_path, pic_path):
    pic_name = csv_file+"_词云图.png"
    path = os.path.abspath(os.curdir)
    csv_file = path+ "\\" + csv_file + ".csv"
    csv_file = csv_file.replace('\\', '\\\\')
    d = pd.read_csv(csv_file, engine='python', encoding='utf-8')
    content = []
    for i in d['content']:
        try:
            i = translate(i)
        except AttributeError as e:
            continue
        else:
            content.append(i)
    comment_after_split = jieba.cut(str(content), cut_all=False)
    wl_space_split = " ".join(comment_after_split)
    backgroud_Image = plt.imread(pic_path)
    stopwords = STOPWORDS.copy()
    with open(stopwords_path, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            stopwords.add(i.strip('\n'))
        f.close()

    wc = WordCloud(width=1024, height=768, background_color='white',
                   mask=backgroud_Image, font_path="C:\simhei.ttf",
                   stopwords=stopwords, max_font_size=400,
                   random_state=50)
    wc.generate_from_text(wl_space_split)
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file(pic_name)

def main(csv_file, stopwords_path, pic_path):
    word_cloud(csv_file,stopwords_path, pic_path)


if __name__ == '__main__':
    main("我不是药神", "stopwords_2.txt", "xuzheng.jpg" )
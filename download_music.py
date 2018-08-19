#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-04 22:06:39
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import requests
import urllib
import json
import io
import sys
import requests
import re
import json
import os


def get_name(singer):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    params = {
        'catZhida': '1',
        'w': singer,
    }
    headers = {
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    html = requests.get(url, headers=headers, params=params).text
    content = re.compile('callback\((.*)\)').findall(html)[0]
    content = json.loads(content)
    data = content.get('data')
    song = data.get('song')
    lists = song.get('list')
    name = []
    for list in lists:
        singer = list.get('singer')[0].get('mid')
        name.append(singer)
    name = name[0]
    return name


def get_html(name, singer):
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg'
    params = {
        'singermid': name,
        'order': 'listen',
        'begin': '0',
        'num': '30',
    }
    headers = {
        'referer': 'https://y.qq.com/n/yqq/singer/003aQYLo2x8izP.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    html = requests.get(url, headers=headers, params=params).text
    return html


def get_music(vkey, songname, filename, singer):
    if vkey and songname:
        url3 = 'http://dl.stream.qqmusic.qq.com/' + filename + \
            '?vkey=' + vkey + '&guid=7133372870&uin=0&fromtag=66'

        headers = {
            'referer': 'https://y.qq.com/n/yqq/singer/003aQYLo2x8izP.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        music = requests.get(url3, headers=headers).content
        dir = singer
        if not os.path.exists(dir):
            os.mkdir(dir)
        with open(dir + '/' + songname + '.m4a', 'wb') as f:
            f.write(music)
        print(songname, '__', singer)


def get_vkey(strMediaMid, songmid, songname, singer):
    if strMediaMid and songmid and songname:
        url2 = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg'
        params = {
            'g_tk': '5381',
            'jsonpCallback': 'MusicJsonCallback8571665793949388',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq',
            'needNewCode': '0',
            'cid': '205361747',
            'callback': 'MusicJsonCallback8571665793949388',
            'uin': '0',
            'songmid': songmid,
            'filename': 'C400' + strMediaMid + '.m4a',
            'guid': '7133372870'
        }
        headers = {
            'referer': 'https://y.qq.com/portal/player.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        detail_html = requests.get(url2, headers=headers, params=params).text
        vkey_disc = re.compile(
            'MusicJsonCallback8571665793949388\((.*?)\)').findall(detail_html)[0]
        vkey_disc = json.loads(vkey_disc)

        data = vkey_disc['data']
        items = data.get('items')[0]
        vkey = items.get('vkey')
        get_music(vkey, songname, 'C400' + strMediaMid + '.m4a', singer)


def get_list(detail_html, singer):
    if detail_html:
        lists = re.compile(
            'data\":{\"list\":(.*?),\"singer_id', re.S).findall(detail_html)[0]
        datas = json.loads(lists)
        for data in datas:
            musicData = data.get('musicData')
            strMediaMid = musicData.get('strMediaMid')
            songmid = musicData.get('songmid')
            songname = musicData.get('songname')
            get_vkey(strMediaMid, songmid, songname, singer)


def main():
    singer = input('请输入歌手姓名：')
    name = get_name(singer)
    detail_html = get_html(name, singer)
    get_list(detail_html, singer)


if __name__ == '__main__':
    main()

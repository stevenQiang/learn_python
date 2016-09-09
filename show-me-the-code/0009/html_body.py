# -*- coding: utf-8 -*-
# 第 0008 题：一个HTML文件，找出里面的正文。
import requests
import urllib2
# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
from bs4 import BeautifulSoup


def html_body(url):
    r = urllib2.urlopen(url)
    html = BeautifulSoup(r)
    for link in html.find_all('a'):
        if str(link.get('href'))[0] != '#':
            print link.get('href')

if __name__ == "__main__":
    url = 'http://docs.python-requests.org/zh_CN/latest/user/advanced.html'
    html_body(url)

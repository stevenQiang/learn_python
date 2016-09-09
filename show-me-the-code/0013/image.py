# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


def get_image(url):
    r = urllib2.urlopen(url)
    html = BeautifulSoup(r)
    for i in html.find_all('img'):
        print i.get('src')


if __name__ == "__main__":
    url = 'http://auto.sohu.com/20160908/n467993199.shtml'
    get_image(url)

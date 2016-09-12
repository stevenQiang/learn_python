# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


def get_momentum_image(url):
    f = urllib2.urlopen(url)
    html = BeautifulSoup(f)
    background_url = html.find(id='background')
    print background_url

if __name__ == '__main__':
    url = 'https://momentumdash.com/'
    get_momentum_image(url)

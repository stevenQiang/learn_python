# -*- coding: utf-8 -*-
import requests
from selenium import webdriver


def get_momentum_image():
    # url = 'chrome://newtab'
    # result = requests.get(url)
    driver = webdriver.Chrome('chrome://newtab')
    print driver

if __name__ == '__main__':
    get_momentum_image()

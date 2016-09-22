# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup


def yield_chapter():
    pass


def get_chapter(url):
    result = urllib2.urlopen(url)
    html = BeautifulSoup(result)
    contents = (html.find_all("dd"))[0: -2]
    book_chapter = {}
    for i in contents:
        book_chapter[i.string] = url + str(i.a['href'])
    print book_chapter


def get_chapter_contents(chapter_name, url):
    result = urllib2.urlopen(url)
    html = BeautifulSoup(result)
    contents = html.find(id="content")
    # text = contents.text.replace('readx();', '')
    f = open(str(chapter_name)+'.txt', 'w+')
    f.write(''.join([i.encode('utf-8') for i in contents.contents[1: -1]]))
    f.close()

if __name__ == '__main__':
    # url = 'http://www.biquge.la/book/176/6660323.html'
    url = 'http://www.biquge.la/book/176/'
    get_chapter(url)

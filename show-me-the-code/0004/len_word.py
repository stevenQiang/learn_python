# -*- coding: utf-8 -*-
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
# 主要利用正则表达式
import re


def len_word(file_name):
    f = open(file_name, 'rb')
    txt = f.read()
    # \S 代表非空。把所有的非空字符串都放到数组里
    words = re.findall(r"\S+", txt)
    return len(words)

if __name__ == '__main__':
    length = len_word('content_word.txt')
    print length

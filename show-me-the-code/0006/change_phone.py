# -*- coding: utf-8 -*-
# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os, re
# 得到一个list里面重复的字符串的个数
from collections import Counter

TXT_TYPE = ['txt']


def phone_list(path='./'):
    # 利用os.listdir()来获得某个目录下面的所有文件
    for i in os.listdir(path):
        photo_split = i.split('.')
        if len(photo_split) >= 2 and photo_split[-1] in TXT_TYPE:
            txt_dir = os.path.join(path, i)
            f = open(txt_dir, 'rb')
            info = f.read()
            # 得到重复的字符串的个数
            counter_list = Counter(re.findall('\S+', info)).most_common()
            # 利用most_common转换成list
            print "filename:"+txt_dir+",name:"+counter_list[0][0]+",number:" + str(counter_list[0][1])
            f.close()


if __name__ == '__main__':
    phone_list('./Journal')

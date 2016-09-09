# -*- coding: utf-8 -*-
# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

TXT_TYPE = ['py', 'js']


def phone_list(path='./'):
    # 利用os.listdir()来获得某个目录下面的所有文件
    for i in os.listdir(path):
        photo_split = i.split('.')
        if len(photo_split) >= 2 and photo_split[-1] in TXT_TYPE:
            txt_dir = os.path.join(path, i)
            f = open(txt_dir, 'rb')
            count = 0
            backspace = 0
            note = 0
            for i in f.readlines():
                i = i.strip()
                count += 1
                if not i:
                    backspace += 1
                elif i.startswith('#') or i.startswith('//'):
                    note += 1
            print "file name is %s, code_number is %s, backspace number is %s, note number is %s" %(txt_dir, count, backspace, note)
            f.close()


if __name__ == '__main__':
    dir_path = "./"
    phone_list(dir_path)

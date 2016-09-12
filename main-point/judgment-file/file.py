# -*- coding: utf-8 -*-
import os


def file_judgment(filename):
    # 用来查看文件存不存在
    return os.path.isfile(filename)


if __name__ == "__main__":
    filename = 'test.py'
    print file_judgment(filename)

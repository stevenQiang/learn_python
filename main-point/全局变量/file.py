# -*- coding: utf-8 -*-
glob_val = 0


def set_global_val():
    # 设置全局变量
    # 全局变量只是指对于本文件而言
    global glob_val
    glob_val = 10


def print_global():
    print glob_val

set_global_val()
print_global()

# -*- coding: utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# string模块提供一些字符串的方便，和变量
# random的基本用法可以看 http://my.oschina.net/cuffica/blog/33336
import random, string


def get_string_list(num=200, length=10):
    f = open('code_list.txt', 'wb')
    charts = string.digits + string.letters
    code_list = []
    for i in range(num):
        # 生成不一样的
        while True:
            code = ''.join([random.choice(charts) for i in range(length)])
            if code in code_list:
                continue
            else:
                f.write(code+'\n')
                code_list.append(code)
                break
    print code_list
    f.close()

if __name__ == '__main__':
    get_string_list()

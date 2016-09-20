# -*- coding: utf-8 -*-


def func(a):
    return {
        'a': 1,
        'b': 2,
        'c': 3
    }.get(a, 4)   # get可以设置一下默认值，如果没有找到的话，默认值就是4

if __name__ == "__main__":
    print func('4')

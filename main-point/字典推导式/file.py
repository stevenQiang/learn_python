# -*- coding: utf-8 -*-


def func(func_list):
    # 把一个list转成一个dict
    print {key: value for (key, value) in enumerate(func_list)}


if __name__ == '__main__':
    func_list = ['a', 'b', 'c', 'd']
    func(func_list)

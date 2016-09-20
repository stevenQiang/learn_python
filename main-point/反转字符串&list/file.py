# -*- coding: utf-8 -*-


def func(func_name):
    # 这种方法适合于list和str都可以进行逆序，利用切片的原理
    print func_name[::-1]


if __name__ == '__main__':
    func_name = "abcdefg"
    func_name2 = [1, 2, 3, 4, 5, 6, 7, 8]
    func(func_name)
    # 如果是list的话，可以用reverse()内建方法来做
    func_name2.reverse()
    print func_name2

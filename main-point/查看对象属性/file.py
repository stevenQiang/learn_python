# -*- coding: utf-8 -*-


# 获取对象属性，可以用dir来查看这个对象的所有属性
def func(a):
    print hasattr(a, 'items')
    print hasattr(a, 'b')

if __name__ == '__main__':
    a = {'a': 2}
    func(a)

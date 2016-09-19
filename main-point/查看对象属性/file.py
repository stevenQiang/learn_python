# -*- coding: utf-8 -*-


def func(a):
    print hasattr(a, 'items')
    print hasattr(a, 'b')

if __name__ == '__main__':
    a = {'a': 2}
    func(a)

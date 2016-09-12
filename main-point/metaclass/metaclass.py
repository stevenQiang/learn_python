# -*- coding: utf-8 -*-
# 元类就是type


def metaclass():
    class MetaClass(object):
        def __init__(self):
            self.a = 1

        def ___metaclass__(self):
            return type('MetaClass', (), self)
    meta = MetaClass()
    print meta.a


if __name__ == "__main__":
    # str创建了一个字符串对象，int创建了一个整形对象，type创建了一个类对象
    Foo = type('Foo', (), {'a': 1})  # 这样就创建了一个类, type就是一个元类，type是python中所有创建类的元类。
    a = 6
    print a.__class__.__class__  # <type 'type'>  就是元类
    metaclass()

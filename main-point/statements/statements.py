# -*- coding: utf-8 -*-
# python中什么都是对象，包括函数


def test1(fn):
    def test1(a, b):
        return "<a>" + fn(1, 2) + "</a>"

    return test1


def test2(fn):
    def test2(a, b):
        return "<div>" + fn(3, 4) + "</div>"

    return test2


# 多个装饰器的话，先把里面看成一个整体来执行，然后一层一层来做，这样就是我们的答案
# 装饰器的话，先执行里面的，然后再执行外面的
@test2
@test1
def foo(a, b):
    print a, b
    return "hello world"


a = foo(2, 3)
print a
# <a><div>hello world</div></a>

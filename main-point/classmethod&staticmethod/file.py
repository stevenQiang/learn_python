# -*- coding: utf-8 -*-

# 当我们需要用一个类里面的某个方法的时候，必须要实例化对象，这样不方便。而classmethod和staticmethod是不需要实例化对象就能使用的。
# 直接使用类名.方法()来调用。
# staticmethod不需要自身的self或cls参数，就跟使用函数一样。
# classmethod需要表示自身类的cls参数。


class A(object):
    def foo(self, x):
        print "executing foo(%s,%s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        cls.foo(x)
        print "executing class_foo(%s,%s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        A.foo(x)
        print "executing static_foo(%s)" % x

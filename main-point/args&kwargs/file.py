# -*- coding: utf-8 -*-


# 允许你使用多个没有定义的参数名
def func_kwargs(**kwargs):
    print kwargs


# 允许你传递多个没有定义的参数
def func_args(*args):
    print args

if __name__ == "__main__":
    func_kwargs(a=1, b=2)
    func_args(1, 2, 3, 4, 5)

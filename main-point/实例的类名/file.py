# -*- coding: utf-8 -*-


def func(func_name):
    # 通过type去获取实例的类名
    print type(func_name).__name__
    # 通过__class__去拿到类名
    print func_name.__class__.__name__

if __name__ == "__main__":
    name = {'a': 1}
    func(name)

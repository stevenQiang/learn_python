# -*- coding: utf-8 -*-
import cProfile


def func():
    print 1111


if __name__ == "__main__":
    # 查看一个脚本运行了多长时间，然后在外面用python去跑脚本的时候，用python -m cProfile fileName.py
    # 或者 可以在执行的时候用cProfile.run('func()')
    func()

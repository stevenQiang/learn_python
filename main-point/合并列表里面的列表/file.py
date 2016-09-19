# -*- coding: utf-8 -*-


def func(demo_list):
    return [a for item in demo_list for a in item]

if __name__ == "__main__":
    func([[1, 2, 3, 4, 5, 6], [4, 5, 6], [7], [8, 9]])




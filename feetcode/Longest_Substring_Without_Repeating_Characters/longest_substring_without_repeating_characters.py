# -*- coding: utf-8 -*-


def longest_string(s):
    result, left, last = 0, 0, {}
    # left用于记录合法的左边界位置，last用于记录字符上一次出现的位置
    for index, value in enumerate(s):
        if value in last and last[value] >= left:
            left = last[value] + 1
        last[value] = index
        print last, left
        result = max(result, index - left + 1)
    return result

if __name__ == '__main__':
    s = "abcbad"
    print longest_string(s)

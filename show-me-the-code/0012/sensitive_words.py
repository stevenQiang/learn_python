# -*- coding: utf-8 -*-
#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

import re


def word_replace(replace_string, word):
    return replace_string.replace(word, "**")


def sensitive_word(input_string):
    f = open('filtered_words.txt', 'rb')
    sensitive_list = (f.read()).split('\n')
    # result = re.sub(str(sensitive_list), '*', input_string)
    for word in sensitive_list:
        input_string = word_replace(input_string, word)
    return input_string

if __name__ == '__main__':
    word = raw_input("please input string: ")
    print sensitive_word(word)

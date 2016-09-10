# -*- coding: utf-8 -*-
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def sensitive_word(input_word):
    f = open('filtered_words.txt', 'rb')
    sensitive_list = (f.read()).split('\n')
    return "Freedom" if input_word in sensitive_list else "Human Rights"

if __name__ == '__main__':
    word = raw_input("please input word: ")
    print sensitive_word(word)

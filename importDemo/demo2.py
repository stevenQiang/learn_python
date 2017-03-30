# -*- coding: utf-8 -*-
from collections import Counter
import re


def get_words(content):
    rule = re.compile(r'\w+')
    words = re.findall(rule, content)
    counter = Counter(words)
    print(counter.most_common()[0])

if __name__ == '__main__':
    get_words('i come from china, china no 1')

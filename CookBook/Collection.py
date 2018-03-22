#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Collection.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 14:22:27 2018
'''
from collections import OrderedDict, defaultdict

if __name__ == '__main__':
    de = defaultdict(set)
    de['a'].add(1)
    de['a'].add(2)
    de['b'].add(3)
    print(de)

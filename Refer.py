#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Refer.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  2/20 22:31:26 2019
'''


from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = a
print(getrefcount(b))

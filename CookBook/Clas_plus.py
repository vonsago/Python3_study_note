#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Clas_plus.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  8/21 12:49:38 2018
'''

#单例模式
class Singleton(object):
    def __new__(cls, *args, **kargv):
        if not hasattr(cls, "_instance"):
            origin = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kargv)
        return cls._instance
class MyClass(Singleton):
    a = 1



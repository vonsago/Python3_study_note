#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Func.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/30 16:38:28 2018
'''

from functools import partial
'''
---note 1---functools.partial
在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一 行的迭代
'''




if __name__ == '__main__':
    RECORD_SIZE = 32
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'') 
        for r in records:
            print(r)


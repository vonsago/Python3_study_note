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
functools.partial 用来创建一个每次被调用时从文件中读取固定数
目字节的可调用对象。标记值 b'' 就是当到达文件结尾时的返回值

在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代

也可使用 partial() 函数来固定某些参数值

'''


def test(a, b, c, d):
    return a, b, c, d


if __name__ == '__main__':
    #RECORD_SIZE = 32
    #with open('somefile.data', 'rb') as f:
    #    records = iter(partial(f.read, RECORD_SIZE), b'') 
    #    for r in records:
    #        print(r)

    s = partial(test, 1,d=4)
    print(s(2,3))

#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Sort.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/23 10:03:24 2018
'''
from operator import itemgetter
'''note 1 对字典列表排序
itermgetter()
>>> l = [1,2,3]
>>> f = itemgetter(0,2)
>>> f(l)
(1, 3)
>>>

'''
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

if __name__== '__main__':

    rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
    print(rows_by_lfname)
    print('---note 1---')


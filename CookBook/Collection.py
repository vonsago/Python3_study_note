#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Collection.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 14:22:27 2018
'''
from collections import OrderedDict, defaultdict \
        ,namedtuple
'''
---note 1 OrderedDict
创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序

---note 2 defaultdict
一个键对应多个值的字典

---note 3 namedtuple



'''

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price 
    return total

if __name__ == '__main__':
    de = defaultdict(set)
    de['a'].add(1)
    de['a'].add(2)
    de['b'].add(3)
    print(de)
    print('---ntoe 1---')
    ord = OrderedDict()
    ord['foo'] = 1
    ord['bar'] = 2
    ord['spam'] = 3 
    ord['grok'] = 4
    oo = {}
    oo['foo'],oo['bar'],oo['spam'],oo['grok']=1,2,3,4
    print(ord)
    print('simple dict:',oo)
    print('---note 2---')

    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    s = Stock('ACME', 100, 123.45)
    s = s._replace(**{'shares':75}) # or 'shares'=75
    print(s)

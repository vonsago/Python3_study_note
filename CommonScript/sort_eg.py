#!/usr/bin/env python
# coding=utf-8
'''
> File Name: sort_eg.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  4/22 20:59:29 2019
'''
import operator
mydict={ 'Li': ['M',7],
'Zhang': ['E',2],
'Wang': ['P',3],
'Du': ['C',2],
'Ma': ['C',9],
'Zhe': ['H',7] }
sorted(mydict.iteritems(), key=lambda (k,v): operator.itemgetter(1)(v))”


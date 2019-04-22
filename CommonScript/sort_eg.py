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


gameresult = [{ "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
...             { "name":"David", "wins":3, "losses":5, "rating":57.00 },
...             { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
...             { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
>>> from operator import itemgetter
>>> sorted(gameresult , key=operator.itemgetter("rating","name"))”


#!/usr/bin/env python
# coding=utf-8
'''
> File Name: List.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 18:03:31 2018
'''
from collections import Counter
from operator import itemgetter
'''note 1 列表元素去重
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
>>>
key 函数参数模仿了 sorted() , min() 和 max() 等内置函数的相似功能
'''
'''note 2 slice
内置函数，切片对象
>>> a = slice(5, 50, 2)
>>> s = 'HelloWorld'
>>> a.indices(len(s))
(5, 10, 2)
>>> for i in range(*a.indices(len(s))):
... print(s[i])
...
W
r
d
通过调用切片的 indices(size) 方法将它映射到一个确定大小的序 列上，这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以 满足边界限制，从而使用的时候避免出现 IndexError 异常
'''

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    l1=list(dedupe(a, key=lambda d: (d['x'],d['y'])))
    print(l1)
    l2=list(dedupe(a, key=lambda d: d['x']))
    print(l2)

    print('---note 1---')
    a = slice(2, 5)
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l[a])
    print('---note 2---')
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    morewords = ['why','are','you','not','looking','in','my','eyes']
    word_counts = Counter(words)
    # 出现频率最高的 3 个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    print('the',word_counts['the'])
    word_counts.update(morewords)
    print(word_counts)
    '''
    同类之间可以进行+ - :w

    '''
    print('---note 3---')


#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Collection.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 14:22:27 2018
'''
import collections
import bisect
from collections import OrderedDict, defaultdict , namedtuple \
        , ChainMap, deque, Counter
'''
---note 1 OrderedDict
创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序

---note 2 defaultdict
一个键对应多个值的字典

---note 3 namedtuple

---note 4 ChainMap
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并 不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重 新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的
>>> len(c)
3
>>> list(c.keys()) ['x', 'y', 'z']
>>> list(c.values()) [1, 2, 3]
如果出现重复键，那么第一次出现的映射值会被返回
对于字典的更新或删除操作总是影响的是列表中第一个字典
ChainMap 使用原来的字典，它自己不创建新的字典(意味着更新原字典会影响ChainMap的结果)

update()
a.update(b)用于合并两个字点

---note 5 Counter

---note 6 deque
和列表很相似，但是插入删除的效率会提高

---note 7
自定义容器


'''

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# DIY collections

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []
    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]
    def __len__(self):
        return len(self._items)
    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


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

    print('---note 3---')
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    c = ChainMap(a,b)
    print(c)
    print ('---note 4---')
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
    '同类之间可以+ - '
    print('---note 5---')
    de = deque('123')
    print(de.pop())
    print('---note 6---')
    
    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[0], items[-1]) 
    items.add(2)
    print(list(items))
    print('---note 7---')

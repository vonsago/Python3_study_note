#!/usr/bin/env python
# coding=utf-8
'''
> File Name: List.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 18:03:31 2018
'''

from collections import Counter

'''
---note 1 列表元素去重
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
>>>
key 函数参数模仿了 sorted() , min() 和 max() 等内置函数的相似功能

---note 2 slice
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

---note 3列表推导与过滤
列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结 果集，占用大量内存
可以使用生成器表达式迭代产生 过滤的元素
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x1006a0eb0> 
>>> for x in pos:
... print(x)

filter()
filter() 函数创建了一个迭代器,需要list()才能得到对应的列表

itertools.compress()
它以一个 iterable 对象和一个相对应的Boolean选择器序列作为输入参数。然后输出iterable对象中对 应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候， 这个函数是非常有用的。
>>> addresses = [
...     '5412 N CLARK',
...     '5148 N CLARK',
...     '5800 E 58TH',
...     '2122 N CLARK',
...     '5645 N RAVENSWOOD',
...     '1060 W ADDISON',
...     '4801 N BROADWAY',
...     '1039 W GRANVILLE',
... ]
>>> counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
>>> from itertools import compress
>>> for i in compress(addresses, [i>5 for i in counts]):
...     print(i)
... 
5800 E 58TH
1060 W ADDISON
4801 N BROADWAY
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
    values = ['1', '2', '-3', '-', '4', 'N/A', '5'] 
    def is_int(val):
        try:
            _ = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values)) 
    print(ivals)

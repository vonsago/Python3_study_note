#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Iter.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/29 09:33:59 2018
'''
#itertools.compress 
#itertools.islice适用于在迭代器和生成器上做切片操作
#itertools.permutation它接受一个集合并产生一个元组序列，每个元组由集合中所有 元素的一个可能排列组成
#itertools.combinations() 可得到输入集合中元素的所有的组合
#itertools.chain 
'''
---note 1---支持迭代操作的自定义对象
目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数
实现一个以深度优先方式遍历树形节点的生成器
使用 yield from 语句返回对应元素

---note 2---
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

--note 3---
>>> from itertools import chain >>> a = [1, 2, 3, 4]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
... print(x)

'''
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node): 
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()




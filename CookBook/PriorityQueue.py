#!/usr/bin/env python
# coding=utf-8
'''
> File Name: PriorityQueue.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 11:03:00 2018
'''

'''note 1:The Diff of __str__ and __repr__:
>>> class Item:
...     def __init__(self, s):
...             self.name = s
...     def __repr__(self):
...             return '[repr: {!r}]'.format(self.name)
...     def __str__(self):
...             return '[str: {!r}]'.format(self.name)
... 
>>> Item('123')
[repr: '123']
>>> print(Item('123'))
[str: '123']

>>> class item:
...     pass
...
>>> item()
<__main__.item object at 0x1040d1198>

二者都是定制类
直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的

fromat()
 “!r” 对应 repr()； “!s” 对应 str(); “!a” 对应 ascii()
'''
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item{!r}'.format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q._queue)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

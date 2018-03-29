#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Iter.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/29 09:33:59 2018
'''

'''
---note 1---支持迭代操作的自定义对象
目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数
实现一个以深度优先方式遍历树形节点的生成器
使用 yield from 语句返回对应元素
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




#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Dict.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 15:09:27 2018
'''
'''note 1 在数据字典中执行一些计算操作
注意
执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys()) print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
'''
'''note 2 两个字典中寻找相同点

'''

if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)
    print('-----')

    a = {
        'x': 1,
        'y': 2,
        'z': 3}
    b = {
        'w': 10,
        'x': 11,
        'y': 2}
    # Find keys in common
    a.keys() & b.keys()  # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys()  # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items()  # { ('y', 2) }

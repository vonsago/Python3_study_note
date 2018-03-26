#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Dict.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 15:09:27 2018
'''
'''
---note 1 在数据字典中执行一些计算操作
注意
执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys()) 
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

---note 2 两个字典中寻找相同点
items()
以列表返回可遍历的(键, 值) 元组数组


---note 3 * **
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# first with *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3

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
    print('---note 1---')

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

    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
    # is twice as fast as this
    p1 = dict((key, value) for key, value in prices.items() if value > 200)

    tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
    p2 = { key:prices[key] for key in prices.keys() & tech_names }

    print('---note 2---')


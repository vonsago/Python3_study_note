#!/usr/bin/env python
# coding=utf-8
'''
> File Name: List.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  3/22 18:03:31 2018
'''

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
列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存
可以使用生成器表达式迭代产生过滤的元素
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x1006a0eb0> 
>>> for x in pos:
... print(x)

filter()
filter() 函数创建了一个迭代器,需要list()才能得到对应的列表


---note 4 reversed
反向迭代一个序列
反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊 方法时才能生效。如果两者都不符合，那你必须先将对象转换为一个列表才行

注意
如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量内存


---note 5 ---enumerate()
迭代一个序列的同时跟踪正在被处理的元素索
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
    values = ['1', '2', '-3', '-', '4', 'N/A', '5'] 
    def is_int(val):
        try:
            _ = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values)) 
    print(ivals)
    print('---note 3---')
    a = [1,2,3,4]
    for i in reversed(a):
        print(i)
    print('---note 4---')

    a = list('abcd')
    for i in enumerate(a):
        print(i)
    print('---note 5---')

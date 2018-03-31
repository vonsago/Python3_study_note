#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Clas.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 六  3/31 15:06:21 2018
'''

import math
'''
8.3
---note 1 ---
__format__

__enter__
__exit__
__slots__

__private 和 __private_method

super()
---note 2--- @property
property 的一个关键特征是它看上去跟普通的 attribute 没什么两样，但是访问它 的时候会自动触发 getter 、setter 和 deleter 方法
Properties 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会 被实际的存储，而是在需要的时候计算出来

---note 3 --- 描述器类
一个描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类
'''
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day): 
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

class Person:
    def __init__(self, first_name):
        self.first_name = first_name
        print('init')
    # Getter function
    @property
    def first_name(self):
        print('getter')
        return self.first_n
    # Setter function
    @first_name.setter
    def first_name(self, value):
        print('setter')
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.first_n = value
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

class Circle:
    def __init__(self, radius): 
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls): 
        if instance is None:
            return self 
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value): 
        if not isinstance(value, int):
            raise TypeError('Expected an int') 
        instance.__dict__[self.name] = value
        print(type(instance),instance.__dict__)
    def __delete__(self, instance):
        del instance.__dict__[self.name]
class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.__dict__)

if  __name__ == '__main__':
    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d) )
    print('The date is {:mdy}'.format(d) )
    print('---note 1---')

    a = Person('Guide')
    print(a.first_name)
    a.first_name = 'Set'
    print(a.first_name)
    print('---note 2---')
    p = Point(2, 3) 
    print('---note 3---')

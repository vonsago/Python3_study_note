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
__getattr__ 是在访问 attribute 不存在的时候被调用
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
#---
#* 8.6
class Person:
    def __init__(self, first_name):
        self.first_name = first_name
        print(self.__dict__)
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
#-
class Circle:
    def __init__(self, radius): 
        self.radius = radius
    @property
    def area(self):
        print('normal--')
        return math.pi * self.radius ** 2
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

#---
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


#---
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type 
    def __get__(self, instance, cls):
        if instance is None: 
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
        print(instance.__dict__)
    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
        # Attach a Typed descriptor to the class 
            setattr(cls, name, Typed(name, expected_type))
        return cls 
    return decorate
# Example use
@typeassert(name=str, shares=int, price=float) 
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        print(self.__dict__)

#---5 8.10
class lazyproperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self 
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value) 
            print( instance.__dict__)
            return value
class Circle1:
    def __init__(self, radius):
        self.radius = radius
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
    @lazyproperty
    def perimeter(self): 
        print('Computing perimeter') 
        return 2 * math.pi * self.radius

#-- 简化的数据结构

class BaseStruct:
    _fields = []
    def __init__(self, *args):
        if len(self._fields) != len(args):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
class Struct1(BaseStruct):
    _fields = ['lng','lat']


#-- 代理
class B2:
    def __init__(self):
        self._a = A()
    def bar(self): 
        pass
    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)

# A proxy class that wraps around another object, but # exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)
    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) 
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)
    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)
class Spam:
    def __init__(self, x):
        self.x = x
    def bar(self, y):
        print('Spam.bar:', self.x, y)

#---
#* 8.24
from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width
@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()
    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)
    def add_room(self, room):
        self.rooms.append(room)
    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                    self.living_space_footage,
                    self.style)
    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage
    def __lt__(self, other): 
        return self.living_space_footage < other.living_space_footage


# ---
# * 8.26

import weakref
_spam_cache = weakref.WeakValueDictionary() 
def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s 
    else:
        s = _spam_cache[name]
        return s


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
    s = Stock('a',1,1.1)
    print('---note 4---')
    c = Circle1(5.0)
    print(c.area)
    print(c.__dict__)
    print(c.area)
    c = Circle(1.0)
    print(c.area)
    print(c.__dict__)
    print(c.area)
    print('---note 5---')
    s1 = Struct1(1.1,2.2)
    print(s1.lng,s1.lat,sep=',')
    print('---note 6---')
    s = Spam(2)
    p = Proxy(s)
    print(p.x)
    p.bar(3)
    p.x=37
    print(p.x)


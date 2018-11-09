#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Clas_plus.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  8/21 12:49:38 2018
'''
'''
\	实例方法	类方法	静态方法
a = A()	a.foo(x)	a.class_foo(x)	a.static_foo(x)
A	不可用	A.class_foo(x)	A.static_foo(x)
'''
def foo(x):
    print("executing foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)



#单例模式
class Singleton(object):
    _mapper = {}
    def __new__(cls, zone):
        if zone not in cls._mapper:
            orig = super(Singleton, cls)
            cls._mapper[zone] = orig.__new__(cls)
        return cls._mapper[zone]

    def __init__(self, zone):
        self.zone = zone

    def test(self):
        print(self._mapper,self.zone)
class MyClass(Singleton):
    a = 1


if __name__ == "__main__":
    A.class_foo(1)
    A().foo(2)
    A.static_foo(3)

    s = Singleton("123")
    s.test()
    b = Singleton("333")
    b.test()
    i = Singleton("444")
    i.test()
    print(Singleton("123")._mapper)

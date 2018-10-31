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
    def __new__(cls, *args, **kargv):
        if not hasattr(cls, "_instance"):
            origin = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kargv)
        return cls._instance
class MyClass(Singleton):
    a = 1


if __name__ == "__main__":
    A.class_foo(1)
    A().foo(2)
    A.static_foo(3)

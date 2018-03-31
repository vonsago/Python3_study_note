#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Pick.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 六  3/31 09:39:32 2018
'''

import pickle

'''
---note 1---将python对象序列化成字节流
data = ... # Some Python object 
f = open('somefile', 'wb')
pickle.dump(data, f)

将一个对象转储为一个字符串
s = pickle.dumps(data)

恢复
# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
# Restore from a string
data = pickle.loads(s)

有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象， 比如打开的文件，网络连接，线程，进程，栈帧等等。用户自定义类可以通过提供 __getstate__() 和 __setstate__() 方法来绕过这些限制。如果定义了这两个方法， pickle.dump() 就会调用 __getstate__() 获取序列化的对象。类似的，__setstate__() 在反序列化时被调用。
'''

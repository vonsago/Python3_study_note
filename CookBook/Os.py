#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Os.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/30 17:04:41 2018
'''
'''
---note 1 ---os
>>> import os
>>> path = '/Users/beazley/Data/data.csv'
>>> # Get the last component of the path 
>>> os.path.basename(path)
'data.csv'
>>> # Get the directory name 
>>> os.path.dirname(path) '/Users/beazley/Data'
>>> # Join path components together
>>> os.path.join('tmp', 'data', os.path.basename(path))
'tmp/data/data.csv'
>>> # Expand the user's home directory
>>> path = '~/Data/data.csv'
>>> os.path.expanduser(path)
'/Users/beazley/Data/data.csv'
>>> # Split the file extension 
>>> os.path.splitext(path)
('~/Data/data', '.csv')
对于任何的文件名的操作，你都应该使用 os.path 模块，而不是使用标准字符串 操作来构造自己的代码。特别是为了可移植性考虑的时候更应如此，因为 os.path 模 块知道 Unix 和 Windows 系统之间的差异并且能够可靠地处理类似 Data/data.csv 和 Data\data.csv 这样的文件名。其次，你真的不应该浪费时间去重复造轮子。通常最好 是直接使用已经为你准备好的功能

>>> os.path.exists('/tmp/spam') 
False

>>> os.path.getsize('/etc/passwd')
3669
>>> os.path.getmtime('/etc/passwd') 
1272478234.0
>>> import time
>>> time.ctime(os.path.getmtime('/etc/passwd'))
'Wed Apr 28 13:10:34 2010'
>>>
>>>os.listdir('somedir')
'''
if __name__ == '__main__':
    pass

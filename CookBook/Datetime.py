#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Datetime.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  3/26 09:42:47 2018
'''

from datetime import timedelta, datetime

'''
---note 1---datetime

---note 2---dateutil
'''

if __name__ == '__main__':
    print('为了表示一 个时间段，可以创建一个 timedelta 实例')
    a = timedelta(days=2, hours=6)
    print(a)
    b = timedelta(hours=4.5)
    print(b)
    c = a+ b
    print(c)
    print(c.days,c.seconds,c.total_seconds())
    print('表示指定的日期和时间，先创建一个 datetime 实例然后使用标准的数学 运算来操作它们')
    a = datetime(2018, 3, 26)
    print(a + timedelta(days = 10))
    print(a - datetime(2018,3,22))
    print(datetime.today())
    print('要注意的是 datetime 会自动处理闰年')
    

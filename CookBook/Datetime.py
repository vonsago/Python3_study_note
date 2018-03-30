#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Datetime.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  3/26 09:42:47 2018
'''

from datetime import timedelta, datetime
from pytz import timezone
'''
---note 1---datetime

---note 2---dateutil

---note 3---from pytz import timezone
处理本地化日期的通常的策略先将所有日 期转换为 UTC 时间，并用它来执行所有的中间存储和操作
>>> print(loc_d)
2013-03-10 01:45:00-06:00
>>> utc_d = loc_d.astimezone(pytz.utc) 
>>> print(utc_d)
2013-03-10 07:45:00+00:00
>>> later_utc = utc_d + timedelta(minutes=30) 
>>> print(later_utc.astimezone(central)) 2013-03-10 03:15:00-05:00
>>> pytz.country_timezones['IN'] 
['Asia/Kolkata']

hhhhhh:
注:当你阅读到这里的时候，有可能 pytz 模块已经不再建议使用了
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
    text = '2012-09-20'
    print("注意datetime.strptime 性能较差")
    y = datetime.strptime(text, '%Y-%m-%d')
    print(y)
    print('几乎所有涉及到时区的问题，你都应该使用 pytz 模块')
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print('一旦日期被本地化了，它就可以转换为其他时区的时间了')
    print(loc_d)
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)

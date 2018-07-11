#!/usr/bin/env python
# coding=utf-8
'''
> File Name: dateme.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  7/11 16:20:17 2018
'''


import time
import datetime

DATE_FORMAT = "%Y-%m-%d-%S"

def time2second(dt=datetime.datetime.now()):
    return time.mktime(dt.timetuple())

def second2time(s,date_format = "%Y-%m-%d %H:%M:%S"):
    return time.strftime(date_format, time.localtime( float(s) ) )


if __name__ == "__main__":
    time_now = time2second()
    print(time_now)
    print(second2time(time_now))


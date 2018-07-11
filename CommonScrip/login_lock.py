#!/usr/bin/env python
# coding=utf-8
'''
> File Name: login_lock.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  7/11 16:44:59 2018
'''
import time
import re

def conform_password_time(last_change_password_time,password_period):
    if last_change_password_time + password_period *86400 <= time.time():
        return True
    return False

def conform_password_level(password, password_level):
    levels = {0:0, 1:6, 2:8, 3:10}
    password_level = levels[password_level]
    if len(password) < password_level:
        return False
    if password_level == 8:
        if re.search('[0-9]', password)==None or re.search('[a-z]', password)==None or re.search(['A-Z', password])==None:
            return False
    if password_level == 10:
        if re.search('\W', password)==None:
            return False
    return True

def judge_locking():

    pass


if __name__ == '__main__':
    pass

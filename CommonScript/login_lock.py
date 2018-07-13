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


password_level = {
        0: (0, lambda x: True if re.search('.', x) else False),
        1: (6, lambda x: True if re.search('.', x) else False),
        2: (8, lambda x: False if not re.search('[0-9]', x) or not re.search('[a-z]', x) or not re.search('[A-Z]', x) else True),
        3: (10, lambda x: True if re.search('\W', x) else False)
        }

def conform_password_level(password, level):
    return True if password_level[level][0] <= len(password) and password_level[level][1](password) else False

def update_password():
    pass
def login(name, password, last_login_time, last_fail_times, max_try_times):
    pass

def judge_locking(name, last_login_time, last_fail_times, max_try_times):
    if last_fail_times==0 or time.time()-last_login_time > 86400:
        last_login_time = time.time()
        last_fail_times = 1
    else:
        last_fail_times += 1
    if last_fail_times > max_try_times:
        return False
    #update database table[name]
    return login()


if __name__ == '__main__':
    for i in range(10):
        data = input()
        password , level = data.split(' ')
        print(conform_password_level(password, int(level)))

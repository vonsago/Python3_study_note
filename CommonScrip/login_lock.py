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
        if not re.search('[0-9]', password) or not re.search('[a-z]', password) or not re.search('[A-Z]', password):
            return False
    if password_level == 10:
        if re.search('\W', password)==None:
            return False
    return True

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
    s1 = '123'
    s2 = 'abc'
    s3 = s1+s2
    s4 = s3+ "%*_"

    print(conform_password_level(s1,0))
    print(conform_password_level(s1+s1,1))
    print(conform_password_level(s2+s3+"AWEF",2))
    print(conform_password_level(s4+"DSFGJAS",3))

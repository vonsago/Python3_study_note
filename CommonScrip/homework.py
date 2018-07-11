#!/usr/bin/env python
# coding=utf-8
'''
*************************************************************************
	> File Name: homwork.py
	> Author: vassago
	> Mail: f811194414@gmail.com
	> Created Time: 五 10/20 08:31:38 2017
 ************************************************************************
'''
 
import time
import random

def get_target():
    #生成随机数
    target = []
    for i in range(1000):
        target.append(random.randint(0,1000))
    return sorted(target)

def cal_time(func): #装饰器
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("running time:",func.__name__, t2 - t1)
        return result
    return wrapper

@cal_time
def pu_search(target,list):
    #朴素查找
    for i in list:
        if target == i:
            return 1
    return

@cal_time
def bin_search(val,data_set):
    #low 和high代表下标 最小下标，最大下标
    low=0
    high=len(data_set)-1
    while low <=high:# 只有当low小于High的时候证明中间有数
        mid=(low+high)//2
        if data_set[mid]==val:
            return mid  #返回他的下标
        elif data_set[mid]>val:
            high=mid-1
        else:
            low=mid+1
    return # return null证明没有找到

@cal_time
def pow(x,y):
    result = x
    for i in range(1,y):
        result = result * i

@cal_time
def bin_pow(x,y):
    result = x


def fabo():
    target = [0,1]
    for i in range(2,100):
        target.append(target[i-1]+target[i-2])
    return target

    

if __name__ == '__main__':
    print fabo()


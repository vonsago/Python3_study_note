#!/usr/bin/python

#================================================================
#   Copyright (C) 2020 Sangfor Ltd. All rights reserved.
#   
#   FileName: Thread.py
#   Author: Vassago
#   CreateTime: 2020-03-27
#   Email: vassago.von@gmail.com
#
#================================================================

from concurrent import futures
import threading
import time

def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n)
    print('{}: done with {}'.format(
        threading.current_thread().name,
        n)
    )
    return n

def test():
    s=time.time()
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    results = ex.map(task, range(5, 0, -1))
    print('main: unprocessed results {}'.format(results))
    print('main: waiting for real results')

def add_call_back():


if __name__ == '__main__':
    test()

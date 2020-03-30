#!/usr/bin/python

#================================================================
#   Copyright (C) 2020 Sangfor Ltd. All rights reserved.
#   
#   FileName: Async.py
#   Author: Vassago
#   CreateTime: 2020-03-27
#   Email: vassago.von@gmail.com
#
#================================================================

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())



def corouted():
    def stupid_fib(n):
    	index = 0
    	a = 0
    	b = 1
    	while index < n:
    		sleep_cnt = yield b
    		print('let me think {0} secs'.format(sleep_cnt))
    		time.sleep(sleep_cnt)
    		a, b = b, a + b
    		index += 1
    print('-'*10 + 'test yield send' + '-'*10)
    N = 20
    sfib = stupid_fib(N)
    fib_res = next(sfib)
    while True:
    	print(fib_res)
	    try:
		    fib_res = sfib.send(random.uniform(0, 0.5))
	    except StopIteration:
		    break

import asyncio
import random

async def smart_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.2)
		await asyncio.sleep(sleep_secs)
		print('Smart one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1

async def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.4)
		await asyncio.sleep(sleep_secs)
		print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [
		asyncio.ensure_future(smart_fib(10)),
		asyncio.ensure_future(stupid_fib(10)),
	]
	loop.run_until_complete(asyncio.wait(tasks))
	print('All fib finished.')
	loop.close()

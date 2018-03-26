#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Random.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/23 19:28:20 2018
'''
from random import choice, sample, shuffle, randint, random, getrandbits
'''
---note 1---random.choice
random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算 法，但是你可以通过 random.seed() 函数修改初始化种子

---note 2---ssl

'''



if __name__ == '__main__':
    l = [1,2,3,4,5]
    print('choice',choice(l))
    print('sample',sample(l,3))
    shuffle(l)
    print('shuffle(打乱序列)',l)
    print('randint',randint(0,10))
    print('random',random(0,10))
    print('getrandbits(获取 N 位随机位 (二进制) 的整数)',getrandbits(200))
    




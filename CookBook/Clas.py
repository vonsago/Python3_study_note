#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Clas.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 六  3/31 15:06:21 2018
'''

'''
---note 1 ---
__format__

__enter__
__exit__

'''
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day): 
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


if  __name__ == '__main__':
    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d) )
    print('The date is {:mdy}'.format(d) )


#!/usr/bin/env python
# coding=utf-8
'''
> File Name: log.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:29:50 2018
'''
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

LOG = logging.getLogger(__name__)
def test_log():
    LOG.debug('debug message')  
    LOG.info('info message')  
    LOG.warning('warning message')  
    LOG.error('error message')  
    LOG.critical('critical message')  
    print('---')

if __name__ == "__main__":
    test_log()
    LOG.setLevel(10)
    test_log()
    print(logging.INFO)


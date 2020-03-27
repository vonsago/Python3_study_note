#!/usr/bin/python

#================================================================
#   Copyright (C) 2020 Sangfor Ltd. All rights reserved.
#   
#   FileName: decorate.py
#   Author: Vassago
#   CreateTime: 2020-02-26
#   Email: vassago.von@gmail.com
#
#================================================================


class TryException(object):
    def __init__(self, name=None):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                LOG.info("[Request {}] {} | {} [Error] {}".format(self.name, args, kwargs, e))
        return wrapper




#!/usr/bin/env python
# coding=utf-8
'''
> File Name: Sort.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  3/23 10:03:24 2018
'''
from operator import itemgetter, attrgetter
'''note 1 对字典列表排序
itermgetter()
>>> l = [1,2,3]
>>> f = itemgetter(0,2)
>>> f(l)
(1, 3)
>>>

'''


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g


def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]

        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g


def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj

class User:
        def __init__(self, user_id):
            self.user_id = user_id 
        def __repr__(self):
            return 'User({})'.format(self.user_id)
def sort_notcompare():
    users = [User(23), User(3), User(99)] 
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    #or code like this:
    sorted(users, key=attrgetter('user_id'))

if __name__ == '__main__':

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)
    print('---note 1---')

    sort_notcompare()

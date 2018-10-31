#!/usr/bin/env python
# coding=utf-8
'''
> File Name: i18n.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  7/ 2 14:19:35 2018
'''

import os
import gettext 


APP_NAME = "my_lang"
LOCALE_DIR = os.path.abspath("locale")

# 这条语句会将_()函数自动放到python的内置命名空间中
#gettext.install(APP_NAME, LOCALE_DIR)
# 获取简体中文翻译类的实例
#lang_zh_CN = gettext.translation(APP_NAME, LOCALE_DIR, ["zh_CN"])
# 获取英文翻译类的实例
#lang_en = gettext.translation(APP_NAME, LOCALE_DIR, ["en"])
gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
gettext.textdomain(APP_NAME)
if __name__ == '__main__':
    print(gettext.gettext('hello world!'))

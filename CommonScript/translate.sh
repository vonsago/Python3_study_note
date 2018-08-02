#!/bin/bash

#pybabel extract -F static/i18n/babel.cfg -k lazy_gettext -o static/i18n/messages.pot .

#pybabel update -i static/i18n/messages.pot -d static/i18n/

echo "翻译完成[y/n]"
read nu
if [ $nu = "y" ]; then pybabel compile -d static/i18n/; else echo "没有编译po文件";fi


#pybabel extract -F static/i18n/babel.cfg -k lazy_gettext -o static/i18n/messages.pot .
#
#pybabel update -i static/i18n/messages.pot -d static/i18n/
#
#echo "翻译完成[y/n]"
#read nu
#if [ $nu = "y" ]; then pybabel compile -d static/i18n/; rm -f static/i18nn/messages.pot; else echo "手动执行: pybabel update -i static/i18n/messages.pot -d static/i18n/";fi

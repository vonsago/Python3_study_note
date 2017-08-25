#!//bin/python
# -*- coding: UTF-8 -*-

'''
date: 20170816
@author: fengyufei
'''

from gevent import monkey
monkey.patch_all()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import requests
import time
import gevent
from gevent import pool

URL ='http://www.miui.com/forum.php?mod=forumdisplay&fid=38&typeid=261&typeid=261&filter=typeid&page={0}'
final_url = 'www.miui.com/{0}'

execute_pool = pool.Pool(80)

def request(url):
    i = 0 
    while i<4:
        try:
            r = requests.get(url)
            return r.content
        except:
            print 'retry request time:',i
            i += 1


def get_data(url):
    print 'start process:',url
    try:
        html_data = request(url) 
        target_data_link_list = re.findall('<div class="avatarbox b_rad_8"><a href=(.*?)><img',html_data)
        target_data_title_list = re.findall('class="s xst">(.*?)</a>',html_data)
        for i in xrange(len(target_data_link_list)):
            outstring = final_url.format(target_data_link_list[i][1:-2]) +' , '+ target_data_title_list[i]+'\n'
            f.write(outstring)
    except Exception as e:
        print e
        print 'page request error!'


if __name__ == '__main__':
    st = time.time()
    print st
    f= open('miui_data','w')

    gs = []
    for i in xrange(500):
        url = URL.format(str(i))
        g = execute_pool.apply_async(get_data,args=(url,))
        gs.append(g)
    gevent.joinall(gs)
    
    print 'starttime:',st 
    f.close()
    print 'timecost:', time.time()-st

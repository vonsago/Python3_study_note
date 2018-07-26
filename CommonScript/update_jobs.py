#!/usr/bin/env python
# coding=utf-8
'''
> File Name: update_jobs.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  7/25 19:24:37 2018
'''

import os
import sys
import time
import json

IP = "192.168.101.26"
URL = "http://{ip}/api/v1/namespaces/{namespace}/pods"
COMMON = "curl {url}"
# git rev-parse HEAD

def list_pod_names():
    pods_url = URL.format(ip=IP, namespace="default")
    pods = os.popen(COMMON.format(url=pods_url)).read()
    lis = json.loads(pods)['items']
    pod_names = [i["metadata"]["selfLink"] for i in lis]
    return pod_names

def get_pod_imageVersion(pod_name):
    #print("pod name:",pod_name)
    url = "http://"+IP+pod_name
    version = os.popen(COMMON.format(url=url)).read()
    version=json.loads(version)
    container = version["status"]["containerStatuses"][0]
    image = container['image'].split(':')[-1]
    #name = container['name']
    return image

def check_name_equal(n1,n2):
    n1 = "-".join(n1.split('/')[-1].split('-')[:-2])
    if n1 == n2+'-adapter' or n1 == n2+'-app-broker' or n1==n2+'-controller' or n1==n2+'-worker' or n1==n2+'-ui':
        return True
    return False

def check_updated(app_name, image):
    pnames = list_pod_names()
    for p in pnames:
        if check_name_equal(p,app_name):
            im = get_pod_imageVersion(p)
            if im == image:
                upup.append(p.split('/')[-1])

if __name__ == "__main__":
    # python update_jobs.py dsp-dev develop-31c4e8d api
    app_name = sys.argv[1]
    image = sys.argv[2]
    ty = sys.argv[3]
    for i in range(10):
        upup = []
        check_updated(app_name, image)
        print(upup)
        if ty == 'api' and len(upup) == 4:
            exit(1)
        elif ty == 'ui' and len(upup) == 1:
            exit(1)
        time.sleep(10)

    exit(0)

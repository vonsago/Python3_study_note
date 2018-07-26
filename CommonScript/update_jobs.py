#!/usr/bin/env python
# coding=utf-8
'''
> File Name: update_jobs.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  7/25 19:24:37 2018
'''

import requests
import os
import sys
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
    print("pod name:",pod_name)
    url = "http://"+IP+pod_name
    version = os.popen(COMMON.format(url=url)).read()
    version=json.loads(version)
    print(version)
    container = version["status"]["containerStatuses"][0]
    image = container['image'].split(':')[-1]
    #name = container['name']
    return image

def check_name_equal(n1,n2):
    pass

if __name__ == "__main__":
    app_name = sys.argv[1]
    pnames = list_pod_names()
    for p in pnames:
        if p == app_name:
            get_pod_imageVersion(p)


#    print(r)

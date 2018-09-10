#!/usr/bin/env python
# coding=utf-8
'''
 > File Name: unit_test.py
 > Author: vassago
 > Mail: f811194414@gmail.com
 > Created Time: 一  9/10 11:10:23 2018
'''
from gevent import monkey
monkey.patch_all()

import gevent
from gevent import pool

import requests


headers = {"Accept":"application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOTZiZGEwY2EtZGRhNC00MzcyLWFiOTItNTUzNDQ4MjU1ZjllIiwiZXhwaXJlZF9hdCI6MTUzNjE2NjExMn0._svuRbcUUcs3zT3xsQPKFI07LQPqF6-y3HybyJ5DobQ",
"Connection":"keep-alive",
"Content-Type":"application/json"}

url = 'http://192.168.101.26:31680/v1/instance_group'

def get_bodys(len):
    for x in range(len):
        yield {"parameters":[{"params":[{"id":"name","value":"nginxb{}".format(str(x))},{"id":"clustersize","value":1},{"id":"imagename","value":"nginx:latest"},{"id":"containerport","value":"80"},{"id":"containercmd","value":[]},{"id":"containerparams","value":[]},{"id":"envs","value":[]},{"id":"registryuser","value":""},{"id":"registrypassword","value":""},{"id":"monitorstatus","value":False},{"id":"monitortype","value":"java"},{"id":"monitorport","value":80},{"id":"monitorname","value":""},{"id":"monitorpassword","value":""}],"plan_id":"a874d348-414c-4d9d-838b-6297f7d0617f","space_id":"cd54c37f-3f60-4ac9-b7a3-5e704d8532e2","service_id":"43ae4f73-a11f-4136-8cb1-460987e0ea7f","zone_id":"dc6a02a0-2600-4897-a0d5-dfb4d36aa0bd","binding_instances":[]}]}

bodys = get_bodys(100000)

def request(body):
    r = requests.post(url, headers = headers, json=body)
    print(r)




execute_pool = pool.Pool(1000)
gs = []
for body in bodys:
    g = execute_pool.apply_async(request, args=(body,))
    gs.append(g)
    request(body)

gevent.joinall(gs)

#!/usr/bin/env python
# coding=utf-8

import urllib

#url = 'http://www.animephile.com/mangagallery/Neesan/Volume 01/neesan_v01_{0}.JPG'
#if __name__ == '__main__':
#    for i in range(164,208):
#        u = url.format('%03d'%i)
#        urllib.urlretrieve(u, '/Users/vassagovon/My_code/oopic/{}.jpg'.format(i))
#        print 'ok = {}'.format(i)
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 18/5/23 下午4:09
依赖：pip install requests
"""
import functools
import logging
import os

import requests

LOG = logging.getLogger(__name__)
# csp 地址，管理员账户密码
base_url = os.getenv("CSP_URL", "http://106.75.62.38:31835")
username = os.getenv("CSP_USERNAME", "admin")
password = os.getenv("CSP_PASSWORD", "admin")

# 根据价格计算plan定价：根据下面的资源单价会为每个服务的每个规格配置按月，按年，按时三种价格：

# 下面代表每个cpu,memory,disk,gpu 每月的价格，单位是分
cpu_price = 1000
memory_price = 2000
disk_price = 100
gpu_price = 5000


# 计算每个月价格，根据cpu，memory，disk，gpu值计算
def get_month_price(n):
    price_month = n('cpu') * cpu_price + n('memory') * memory_price / 1024.0 + n('disk') * disk_price + +n(
        'gpu') * gpu_price
    return price_month


# 计算每年价格：默认优化按10个月算
def get_year_price(n):
    return get_month_price(n) * 10


# 计算每时价格：默认是按月计费的3倍计算
def get_hour_price(n):
    return (get_month_price(n) / 30.0 / 24.0) * 3


class CSPClient(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        if self.base_url.endswith('/'):
            self.base_url = self.base_url[:-1]
        self.username = username
        self.password = password

    def _add_auth_header(self, headers=None):
        response = requests.post('{}/v1/login'.format(self.base_url), json={
            "username": self.username,
            "password": self.password
        })
        if response.status_code >= 400:
            LOG.warning('Auto create account error: %s:%s', response.status_code, response.text)
            return None
        if not headers:
            headers = {}
        headers['authorization'] = "Bearer {}".format(response.json()['token'])
        return headers

    def get_all_service(self):
        response = requests.get('{}/v1/services'.format(self.base_url), headers=self._add_auth_header())
        if response.status_code >= 400:
            LOG.warning('get services error: %s:%s', response.status_code, response.text)
            return []
        return response.json()

    def get_all_plan(self, service_id):
        response = requests.get('{}/v1/services/{}/plans'.format(self.base_url, service_id),
                                headers=self._add_auth_header())
        if response.status_code >= 400:
            LOG.warning('get services error: %s:%s', response.status_code, response.text)
            return []
        return response.json()

    def set_plan_price(self, service, plan, charging_rule_details):
        charging_rules = requests.get('{}/v1/charging_rules?product_id={}'.format(self.base_url, plan.get('id')),
                                      headers=self._add_auth_header()).json()
        for charging_rule in charging_rules:
            response = requests.delete('{}/v1/charging_rules/{}'.format(self.base_url, charging_rule.get('id')),
                                       headers=self._add_auth_header())
            LOG.debug('delete charging_rule error: %s:%s', response.status_code, response.text)
        response = requests.post('{}/v1/charging_rules'.format(self.base_url), headers=self._add_auth_header(), json={
            "name": plan.get('name'),
            "description": "",
            "product_id": plan.get('id'),
            "charging_rule_details": charging_rule_details
        })
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()


def get_bullet_by_name(name, bullets=None):
    for bullet in bullets:
        if bullet.get("name", '') == name:
            return bullet.get('value')

    return 0


def init_price():
    csp_client = CSPClient(base_url, username, password)
    for service in csp_client.get_all_service():
        for plan in csp_client.get_all_plan(service.get('id')):
            # [{"name": "cpu", "unit": "core", "value": 0.1}, {"name": "memory", "unit": "m", "value": 8192}, {"name": "disk", "unit": "g", "value": 32}, {"name": "gpu", "unit": "gpu", "value": 0}]
            n = functools.partial(get_bullet_by_name, bullets=plan.get('bullets'))

            price = [
                #     {
                #     "charging_type_code": "once",
                #     "prices": [{"time": "", "price": once_price}]
                # },
                {
                    "charging_type_code": "hourly",
                    "prices": [{"time": "",
                                "price": int(get_hour_price(n))}]
                }, {
                    "charging_type_code": "monthly",
                    "prices": [{"time": "",
                                "price": int(get_month_price(n))}]
                }, {
                    "charging_type_code": "yearly",
                    "prices": [{"time": "",
                                "price": int(get_year_price(n))}]
                }]
            csp_client.set_plan_price(service, plan, price)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)-8s %(message)s')
    init_price()



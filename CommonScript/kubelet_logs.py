#!/usr/bin/env python
# coding=utf-8
'''
> File Name: kubelet_logs.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  7/30 22:46:05 2018
'''
import paramiko

class sshClient():
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def _create_client(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, 22, self.username, self.password, timeout=5)
        return ssh

    def exec_command(self, client, cmd):
        client.exec_command(cmd)

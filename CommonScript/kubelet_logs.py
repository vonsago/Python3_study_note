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

    def _create_client(self, port=22, timeout=5, local_host_key=False):
        ssh = paramiko.SSHClient()
        if not local_host_key:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        else:
            ssh.load_system_host_keys()
        ssh.connect(self.ip, port, self.username, self.password, timeout=timeout)
        return ssh

    def exec_command(self, client, cmd):
        stdin, stdout, stderr = client.exec_command(cmd)
        return stdin, stdout, stderr


if __name__ == "__main__":
    ip = ""
    nclient = sshClient(ip, un, pw)

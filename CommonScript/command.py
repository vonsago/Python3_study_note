#!/usr/bin/env python
# coding=utf-8
'''
> File Name: command.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  4/23 18:01:00 2019
'''
'''
$ pyinstaller -F command.py
$ cp ./dist/command /usr/local/bin/ 
$ command -v
'''

import sys, getopt, argparse

def help():
    print("help")

def get_yaml(fname):
    with open(fname, 'r') as f:
        data = f.read()
        print(data)

def process_create(args):
    if args.input:
        get_yaml(args.input)

def process_get(args):
    pass

def init_parser():
    parser=argparse.ArgumentParser(
        description='''My Description. And what a lovely description it is. ''',
        epilog="""All's well that ends well.""")
    parser.add_argument("-v", "--version", action='store_true', help="increase output verbosity")

    subparsers = parser.add_subparsers(dest="subparser_name")


    parser_create = subparsers.add_parser('create', help='CREATE!')
    parser_create.add_argument('-f', '--input', type=str, help='name of yaml file!')


    args = parser.parse_args()

    if args.version:
        print("ruyiyun openapi 1.0")
    elif args.subparser_name == "create":
        process_create(args)
    elif args.subparser_name == "get":
        process_get(args)


if __name__ == "__main__":
    init_parser()

#!/usr/bin/env python
# coding=utf-8
'''
*************************************************************************
    > File Name: valc.py
    > Author: vassago
    > Mail: f811194414@gmail.com
    > Created Time: 二 11/ 7 18:18:08 2017
 ************************************************************************
'''

import sys 
#get and update the data
def process_args(args):
    #合并，组成正确的小数
    while(1):
        try:
            x=args.index('.')
        except :
            break
        args[x-1]+=args[x]
        args[x-1]+=args[x+1]
        del args[x]
        del args[x]
    #合并，组成正确的多位数
    llen =len(args)
    i=1
    while(i<llen):
        if(args[i-1]=='(' or args[i-1]==')' or args[i-1]=='+' or args[i-1]=='-' or args[i-1]=='*' or args[i-1]=='/' or args[i-1]=='^'):
            i+=1
            continue
        if(args[i]!='(' and args[i]!=')' and args[i]!='+' and args[i]!='-' and args[i]!='*' and args[i]!='/' and args[i]!='^'):
            args[i-1]+=args[i]
            del args[i]
            llen-=1
            i-=1
        i+=1
    return args

def get_nibolan_list(args):
    #get nibolan list
    pri={'(':0,')':0, '+':1,'-':1, '*':2,'/':2,'^':3}
    stack1,stack2=[],[]

    for x in args:
        if(x=='main.py' or x==' '):
            continue
        if(x=='('):
            stack1.append(x)
        elif(x==')'):
            top=stack1.pop()
            while(top!='('):
                try:
                    stack2.append(top)
                    top=stack1.pop()
                except:
                    print("FORMAT ERROR")
                    return 
        elif(x=='+' or x=='-' or x=='*' or x=='/' or x=='^'):
            if(len(stack1)==0):
                stack1.append(x)
            else:
                top1=stack1.pop()
                if(pri[x]>pri[top1]):
                    stack1.append(top1)
                    stack1.append(x)
                else:
                    while(1):
                        if(pri[x]>pri[top1]):
                            stack1.append(top1)
                            break
                        stack2.append(top1)
                        if(len(stack1)==0):
                            break
                        top1=stack1.pop()
                    stack1.append(x)
        else:
            stack2.append(x)

    while(len(stack1)!=0):
        stack2.append(stack1.pop())

    nibolan=[]
    while(len(stack2)!=0):
        nibolan.append(stack2.pop())

    #print(nibolan)
    return nibolan

def process_nibolan(nibolan):
    #output the answer
    stack,fla=[],1
    while(1):
        try:
            top=nibolan.pop()
        except:
            return 
        if(top=='+' or top=='-' or top=='*' or top=='/' or top=='^'):
            try:
                y=float(stack.pop())
                x=float(stack.pop())
            except IndexError:
                print('FORMAT ERROR')
                fla=0
                break
            except ValueError:
                print('INPUT ERROR')
                fla=0
                break

            try:
                if(top=='+'):
                    stack.append(x+y)
                if(top=='-'):
                    stack.append(x-y)
                if(top=='*'):
                    stack.append(x*y)
                if(top=='/'):
                    stack.append(x/y)
                if(top=='^'):
                    assert(x!=0)
                    stack.append(x**y)
            except :
                print('VALUE ERROR')
                fla=0
                break

            while(len(stack)!=0):
                nibolan.append(stack.pop())
        else:
            stack.append(top)
        if(len(nibolan)==0):
            break
    if(fla):
        return stack[0]

if __name__ == '__main__':
    string = ''
    for x in sys.argv[-1]:
        if(x==' '):
            continue
        string+=x

    args=list(string)
    ans = (process_nibolan(get_nibolan_list(process_args(args))))
    if(ans!= None):
        try:
            if(round(ans) == ans):
                print(round(ans))
            else:
                print(round(ans,10))
        except:
            print("VALUE ERROR")

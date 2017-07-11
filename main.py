# -*- coding: UTF-8 -*-
import sys, getopt 

#get and update the data
string=""
for x in sys.argv:
	if(x=="main.py" or x==' '):
		continue
	string+=x

args=list(string)

while(1):
	try:
		x=args.index('.')
	except:
		break
	args[x-1]+=args[x]
	args[x-1]+=args[x+1]
	del args[x]
	del args[x]

#get nibolan list
pri={'(':0,')':0, '+':1,'-':1, '*':2,'/':2,'^':3}
stack1=[]
stack2=[]

for x in args:
	if(x=='main.py' or x==' '):
		continue
	if(x=='('):
		stack1.append(x)
	elif(x==')'):
		top=stack1.pop()
		while(top!='('):
			stack2.append(top)
			top=stack1.pop()
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
#ab+c*ab+e/-

nibolan=[]
stack=[]
fla=1
while(len(stack2)!=0):
	nibolan.append(stack2.pop())

#print(nibolan)

#output the answer
while(1):
	top=nibolan.pop()
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
				stack.append(x**y)
		except ValueError :
			print('Value Error')
			fla=0
			break

		while(len(stack)!=0):
			nibolan.append(stack.pop())
	else:
		stack.append(top)
	if(len(nibolan)==0):
		break
if(fla):
	print(stack[0])
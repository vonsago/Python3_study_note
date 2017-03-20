import sys

def fibon(n):
	a,b,counter=0,1,0
	while True:
		if(counter>n):
			return
		yield a
		a,b=b,a+b
		counter+=1

f=fibon(10)

while True:
	try:
		print(next(f),end=" ")
	except StopIteration:
		sys.exit()
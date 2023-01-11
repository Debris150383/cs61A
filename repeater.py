#!/usr/bin/env python

from operator import add
square = lambda x: x*x
identity = lambda x: x
def accumulate(combiner,base,n,term):
	ret = base
	for i in range(1,n+1):
		ret = combiner(ret,term(i))
	return ret	

def compose1(func1,func2):
	def f(x):
		return func1(func2(x))
	return f

def repeater(func,n):
	return accumulate(compose1,identity,n,lambda y :func) 

if __name__ == '__main__':
	print(repeater(square,4)(5))

#!/bin/usr/env python
def zero(f):
	return lambda x: x

def successor(n):
	return lambda f: lambda x: f(n(f)(x))

def one(f):
	#return successor(zero)
	return lambda x: f(x)

def two(f):
	return lambda x: f(f(x))

def church_to_int(n):
	return n(lambda x: x+1)(0)

def add_church(m,n):
	'''
	int_n = church_to_int(n)
	for i in range(int_n):
		m = successor(m)
	return m
	'''
	return lambda f: lambda x: n(f)(m(f)(x))

def mul_church(m,n):
	return lambda f: n(m(f))

def pow_church(m,n):
	return n(m)	

if __name__ == "__main__":
	print(church_to_int(zero))
	print(church_to_int(one))
	three = successor(two)
	print(three)
	print(church_to_int(add_church(two,three)))
	print(church_to_int(mul_church(two,three)))
	print(church_to_int(pow_church(two,three)))

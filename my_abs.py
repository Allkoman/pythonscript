#!/usr/bin/env python3

def my_abs(x):
	if x >= 0: 
		return x 
	else: 
		return -x

a = input('please input:')

print(my_abs(int(a)))
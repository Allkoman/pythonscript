#!/usr/bin/env python3

import math

def quadratic(a,b,c):
	n = b*b - 4*a*c
	if a==0:
		x = -c/b
		return x
	elif a!=0:
		if n > 0:
			x1 = (-b + math.sqrt(n))/(2*a)
			x2 = (-b - math.sqrt(n))/(2*a)
			return x1,x2
		elif n == 0:
			x = -b/(2*a)
			return x
		else:
			return '无解'

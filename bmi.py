#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = float(input('身高 : '))
b = float(input('体重 : '))

bmi = b/a/a

if bmi < 18.5 :
	print('过轻')
elif bmi <= 25 :
	print('正常')
elif bmi <= 28 :
	print('过重')
elif bmi <= 32 :
	print('肥胖')
elif bmi > 32 :
	print('严重肥胖')	
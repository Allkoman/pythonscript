#!/usr/bin/env python3

def triangles(max):
    L = [1]
    while len(L)<=max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = input('please input the max num : ')
for x in triangles(int(n)):
	print(x)
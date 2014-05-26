#!/usr/bin/env python

# File name: 		projecteuler053.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/26
# Date Modified: 	2014/05/26
# Python Version: 	2.7

def factorial(n):
	while n > 0:
		return n*factorial(n-1)
	if n == 0:
		return 1

def solution053():
	target = 100
	count = 0
	for n in range(23,target+1):
		for r in range(1,n):
			n_choose_r = factorial(n)/(factorial(r)*(factorial(n-r)))
			if n_choose_r > 10**6:
				count += 1

	return count

print solution053()
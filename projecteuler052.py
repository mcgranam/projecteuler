#!/usr/bin/env python

# File name: 		projecteuler052.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/24
# Date Modified: 	2014/05/24
# Python Version: 	2.7

def same_digits(n):
	digits = list(str(n))
	digits.sort()
	for i in range(2,6+1):
		multi_i = n*i
		multi_digits = list(str(multi_i))
		multi_digits.sort()
		if digits != multi_digits:
			return False
	return True

def solution052():
	found = False
	n = 0
	while found == False:
		n += 1
		found = same_digits(n)
	return n

print solution052()
#!/usr/bin/env python

# File name: 		projecteuler057.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/28
# Date Modified: 	2014/05/28
# Python Version: 	2.7

def solution056():
	max_digit_sum = 0
	for a in range(1,100):
		for b in range(1,a):
			digit_sum = sum(map(int,list(str(a**b))))
			if digit_sum > max_digit_sum:
				max_digit_sum = digit_sum
	return max_digit_sum

print solution056()

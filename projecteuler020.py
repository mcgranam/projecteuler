#!/usr/bin/env python

# File name: 		projecteuler020.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/30
# Date Modified: 	2014/04/30
# Python Version: 	2.7

# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def solution020():

	target = 100
	factorial = 1
	for i in range(1,target+1):
		factorial = factorial*i

	sum_digits = sum(map(int,list(str(factorial))))
	return sum_digits

print solution020()
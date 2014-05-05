#!/usr/bin/env python

# File name: 		projecteuler030.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/05
# Date Modified: 	2014/05/05
# Python Version: 	2.7

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def solution030():
	target = 5*9**5
	sum_all = 0

	for i in range(2,target+1):
		sum_fifth = 0
		d = i
		while d > 0:
			sum_fifth += (d%10)**5
			d /= 10
		if i == sum_fifth:
			sum_all += i

	return sum_all


print solution030()

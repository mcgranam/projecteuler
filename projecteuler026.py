#!/usr/bin/env python

# File name: 		projecteuler026.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/03
# Date Modified: 	2014/05/03
# Python Version: 	2.7

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def solution026():
	target = 1000
	remainder_lengths = [None]*target

	for i in range(2,target):
		print i
		remainder_list = []
		remainder = 1
		flag = True
		while flag == True:
			numerator = remainder*(10**(len(str(i-1))))
			remainder = numerator%i
			if remainder == 0:
				flag = False
			elif (remainder in remainder_list):
				remainder_lengths[i] = (len(remainder_list))
				flag = False
			else:
				remainder_list.append(remainder)

	max_cycle = max(remainder_lengths)
	max_denominator = remainder_lengths.index(max_cycle)
	return max_denominator

print solution026()
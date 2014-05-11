#!/usr/bin/env python

# File name: 		projecteuler039.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/11
# Date Modified: 	2014/05/11
# Python Version: 	2.7

def solution039():
	max_count = 0
	max_sols = 0
	max_length = 1000

	for i in range(12,max_length+1):
		count_triangle = 0
		for a in range(i-2,i/3,-1):
			for b in range(min([i-a,a])-1,(i-a)/2,-1):
				c = i-a-b
				if (c**2 + b**2) == (a**2):
					count_triangle += 1
		if count_triangle > max_count:
		 	max_count = count_triangle
		 	max_sols = i

	return max_sols

print solution039()


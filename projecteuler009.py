#!/usr/bin/env python

# File name: 		projecteuler009.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/18
# Date Modified: 	2014/04/18
# Python Version: 	2.7

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def solution009():
	target = 1000
	for m in range(2,1000):
		for n in range(1,m-1):
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			
			if a + b + c == target:
				return a*b*c

print solution009()


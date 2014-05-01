#!/usr/bin/env python

# File name: 		projecteuler021.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/30
# Date Modified: 	2014/04/30
# Python Version: 	2.7

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def solution021():
	target = 10000
	amicable = []
	
	for n in range(1,target+1):
		d1 = []
		for i in range(1,int(n**0.5)+1):
			if n%i == 0:
				d1.append(i)
				d1.append(n/i)
		d1.sort()
		d1.pop(-1)
		s1 = sum(d1)

		d2 = []
		for j in range(1,int(s1**0.5)+1):
			if s1%j == 0:
				d2.append(j)
				d2.append(s1/j)
		d2.sort()
		d2.pop(-1)
		s2 = sum(d2)

		if (n == s2) and (n != s1):
			amicable.append(n)

	sum_amicable = sum(amicable)

	return sum_amicable

print solution021()


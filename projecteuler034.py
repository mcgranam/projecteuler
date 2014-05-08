#!/usr/bin/env python

# File name: 		projecteuler034.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/08
# Date Modified: 	2014/05/08
# Python Version: 	2.7

def factorial(n):
	factorials = [1,1,2,6,24,120,720,5040,40320,362880]
	return factorials[n]

def solution034():
	max_number = factorial(9)*7
	sum_special = 0
	for i in range(3,max_number):
		k = i
		factorial_sum = 0
		while k > 0:
			d = factorial(k%10)
			k = k/10
			factorial_sum += d
		if factorial_sum == i:
			sum_special += i
			print i
	return sum_special

print solution034()


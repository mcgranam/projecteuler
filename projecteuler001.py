#!/usr/bin/env python

# File name: 		projecteuler001.py
# Author: 			Matt McGranaghan
# Date Created: 	2014/04/11
# Date Modified: 	2014/04/11
# Python Version: 	2.7

# Problem 1: Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def solution001():

	sum_multiples = 0
	max_n = 1000

	# Use modular division to find, and add, the multiples of 3 *or* 5. A number that is a multiple of both will also be added - once - to the sum.
	for i in range(1,max_n):
		if i%3 == 0 or i%5 == 0:
			sum_multiples += i

	return sum_multiples

print solution001()
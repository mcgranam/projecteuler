#!/usr/bin/env python

# File name: 		projecteuler006.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/17
# Date Modified: 	2014/04/17
# Python Version: 	2.7

# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def solution006():
	target = 100
	numbers = range(1,target+1)

	sum_of_squares = reduce(lambda x, y: x+y**2, numbers)
	sqaure_of_sums = (reduce(lambda x, y: x+y, numbers))**2
	diff = sqaure_of_sums - sum_of_squares

	return diff

print solution006()

#!/usr/bin/env python

# File name: 		projecteuler032.py
# Author: 		Matt McGranaghan
# Date Created:		2014/05/07
# Date Modified: 	2014/05/07
# Python Version: 	2.7

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import itertools

def solution032():
	perms = [''.join(i) for i in itertools.permutations("123456789")]
	perms = map(int,perms)

	prod_list = []
	for p in perms:
		# 2 x 3 = 4 type
		mcand  = p/10**7
		mplier = (p%10**7)/10**4
		prod   = p%10**4
		if mcand * mplier == prod:
			prod_list.append(prod)

		# 1 x 4 = 4 type
		mcand  = p/10**8
		mplier = (p%10**8)/10**4
		prod   = p%10**4
		if mcand * mplier == prod:
			prod_list.append(prod)

	sum_prod_list = sum(list(set(prod_list)))

	return sum_prod_list

print solution032()

#!/usr/bin/env python

# File name: 		projecteuler028.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/05
# Date Modified: 	2014/05/05
# Python Version: 	2.7

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def solution028():
	target = 1001
	count = 3
	total_sum = 1

	while count <= target:
		ur = count**2
		ul = ur - (count-1)
		ll = ul - (count-1)
		lr = ll - (count-1)
		total_sum += (ur+ul+ll+lr)
		count += 2

	return total_sum

print solution028()

		
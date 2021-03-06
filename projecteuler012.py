
#!/usr/bin/env python

# File name: 		projecteuler012.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/22
# Date Modified: 	2014/04/22
# Python Version: 	2.7

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

def get_num_factors(n):
    num_factors = 0
    for i in range(1, int((n)**0.5)+1):
        if (n % i) == 0:
            num_factors += 2
    return num_factors

def solution012():
	tri_number = 1
	count = 1
	target = 500

	while get_num_factors(tri_number) < target:
		count += 1
		tri_number += count

	return tri_number

print solution012()

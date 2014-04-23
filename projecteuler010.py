#!/usr/bin/env python

# File name: 		projecteuler010.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/22
# Date Modified: 	2014/04/22
# Python Version: 	2.7

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def solution010():
	target = 2000000
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.pop(0)
	prime_numbers = filter(None,prime_numbers)
	return sum(prime_numbers)

print solution010()


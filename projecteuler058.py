#!/usr/bin/env python

# File name: 		projecteuler057.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/29
# Date Modified: 	2014/05/29
# Python Version: 	2.7

def is_prime(n):
	for i in range(2,int(n**(0.5))):
		if n % i == 0:
			return False
	return True

def solution058():
	prime_count = 0
	corner_count = 1
	count = 1

	while (prime_count == 0) or (1.0*prime_count/corner_count) > 0.1:
		count += 2
		ur = count**2
		ul = ur - (count-1)
		ll = ul - (count-1)
		lr = ll - (count-1)
		if is_prime(ul):
			prime_count += 1
		if is_prime(ll):
			prime_count += 1
		if is_prime(lr):
			prime_count += 1
		corner_count += 4
	return count

print solution058()
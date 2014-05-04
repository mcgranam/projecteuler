#!/usr/bin/env python

# File name: 		projecteuler027.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/04
# Date Modified: 	2014/05/04
# Python Version: 	2.7


def prime_list(max_prime):
	target = max_prime
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	return prime_numbers

def solution027():
	max_chain = 0
	target = 1000
	primes = prime_list(100000)
	for a in range(-target,target+1):
		for b in range(-target,target+1):
			n = 0
			quadratic = (n**2 + a*n + b)
			while quadratic == primes[quadratic-1]:
				n += 1
				quadratic = (n**2 + a*n + b)
			if n > max_chain:
				max_coef = [a,b,n]
				max_chain = n

	max_coef_prod = max_coef[0]*max_coef[1]
	return max_coef_prod

print solution027()
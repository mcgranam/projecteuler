#!/usr/bin/env python

# File name: 		projecteuler041.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/12
# Date Modified: 	2014/05/12
# Python Version: 	2.7

def gen_primes(max_prime):
	target = max_prime
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	
	prime_numbers.insert(0,None)
	prime_numbers[1] = None
	return prime_numbers

def solution041():

	max_prime = 7654321
	primes = gen_primes(max_prime)

	max_pan_prime = 0
	for p in range(len(primes)):
		if p != None:
			str_p = str(p)
			if len(set(str_p)) == len(str_p):
				max_pan_prime = p

	return max_pan_prime

print solution041()

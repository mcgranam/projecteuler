#!/usr/bin/env python

# File name: 		projecteuler037.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/10
# Date Modified: 	2014/05/10
# Python Version: 	2.7

def is_trunc(n, prime_numbers):
	mag = len(str(n))
	k = n
	f = n%(10**mag)
	while k > 0:
		if (prime_numbers[f] == None) or (prime_numbers[k] == None):
			return False
		mag = mag-1
		k = k/10
		f = n%(10**mag)
	return True

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

def solution037():
	prime_numbers = gen_primes(1000000)
	trunc_primes = []
	while len(trunc_primes) < 11:
		for p in range(len(prime_numbers)):
			if (p != None) and (p>9):
				if is_trunc(p,prime_numbers):
					trunc_primes.append(p)
	return sum(trunc_primes)

print solution037()



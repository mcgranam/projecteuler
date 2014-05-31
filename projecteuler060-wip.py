#!/usr/bin/env python

# File name: 		projecteuler060.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/31
# Date Modified: 	2014/05/31
# Python Version: 	2.7

def make_primes(max_prime):
	prime_numbers = range(1,max_prime+1)
	for p in range(2,max_prime):
		if prime_numbers[p-1] != None:
			for i in range(p,max_prime/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.insert(0,None)
	prime_numbers[1] = None
	return prime_numbers

def n_pairs(n, prime_list, pairs):
	count_pairs = 1
	for q in range(len(prime_list)):
		if prime_list[q] != None:
			if int(str(n)+str(q)) < len(prime_list):
				if prime_list[int(str(n) + str(q))] != None:
					count_pairs += 1
	if count_pairs == pairs:
		return True
	return False

def main():

	primes = make_primes(1000000)
	pairs = 4
	for p in range(len(primes)):
		print p
		if primes[p] != None:
			count_pairs = 1
			for q in range(p+1,len(primes)):
				if primes[q] != None:
					new_p = int(str(p)+str(q))
					if new_p < len(primes):
						if primes[new_p] != None:
							if n_pairs(q, primes,pairs):
								count_pairs += 1
								if count_pairs == 4:
									return p
			if count_pairs < pairs:
				primes[p] = None
			if count_pairs >= pairs:
				print p, "Hello"

print main()
#!/usr/bin/env python

# File name: 		projecteuler051.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/24
# Date Modified: 	2014/05/24
# Python Version: 	2.7

import itertools
import copy

def primes(max_prime):
	prime_numbers = range(1,max_prime+1)
	for p in range(2,max_prime):
		if prime_numbers[p-1] != None:
			for i in range(p,max_prime/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.pop(0)
	prime_numbers.insert(0,None)
	prime_numbers.insert(1,None)
	return prime_numbers

def find_replaceable_indices(n):
	replaceable_indices_list = []
	indices_string = ""
	for i in range(0,n-1):
		indices_string = indices_string+str(i)
		replaceable_indices_list.append(indices_string)

	replace_indices = []
	for index_list in replaceable_indices_list:
		permutation_list = itertools.permutations(index_list)
		for p in permutation_list:
			indices = [int(p[0])]
			for i in p:
				if int(i) > indices[-1]:
					indices.append(int(i))
			if (indices not in replace_indices) and (len(indices) > 1):
				replace_indices.append(indices)
	return replace_indices

def new_primes(prime_list,i_list):
	new_primes_list = []
	i_list.reverse()
	for p in prime_list:
		p = list(str(p))
		deleted = []
		for i in i_list:
			d = p.pop(i)
			deleted.append(d)
		if len(set(deleted)) == 1:
			new_primes_list.append(p)
	return new_primes_list

def prime_replacement(magnitude,family_size):
	prime_list = primes(10**magnitude)
	prime_numbers = []
	for p in prime_list:
		if (p != None) and (p > 10**(magnitude-1)):
			prime_numbers.append(p)
	replace_list = find_replaceable_indices(magnitude)
	replace_list.sort(lambda x,y: cmp(len(x), len(y)))

	for r in replace_list:
		new_p_list = new_primes(prime_numbers,r)
		for n in new_p_list:
			if new_p_list.count(n) == family_size:
				n = map(int,n)
				return [n,r]

def solution051():
	family_size = 8
	family_found = False
	magnitude = 5
	while family_found == False:
		found = prime_replacement(magnitude, family_size)
		if found:
			smallest_prime = [0]*(magnitude)
			for i in range(magnitude):
				if i in found[1]:
					smallest_prime[i] = 1
				else:
					x = found[0].pop(0)
					smallest_prime[i] = x
			smallest_prime = map(str,smallest_prime)
			smallest_prime = int(''.join(smallest_prime))
			return smallest_prime
		magnitude += 1

print solution051()



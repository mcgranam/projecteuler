#!/usr/bin/env python

# File name: 		projecteuler050.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/20
# Date Modified: 	2014/05/20
# Python Version: 	2.7

def primes(target):
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.pop(0)
	prime_numbers.insert(0,None)
	prime_numbers.insert(1,None)
	return prime_numbers

def solution050():
	prime_list = primes(1000000)
	prime_numbers = filter(None,prime_list)

	max_sum = 0
	max_l = 1
	for i in range(len(prime_numbers)-1):
		l = 1
		j = i+l
		sum_i_j = prime_numbers[i]
		while (sum_i_j + prime_numbers[j]) < prime_numbers[-1]:
			sum_i_j += prime_numbers[j]
			if sum_i_j == prime_list[sum_i_j]:
				if l > max_l:
					max_l = l + 1 # count base element
					max_sum = sum_i_j
			if j < len(prime_numbers):
				l += 1
				j  = i+l
			else:
				break

	return max_l, max_sum

print solution050()


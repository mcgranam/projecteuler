#!/usr/bin/env python

# File name: 		projecteuler035.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/07
# Date Modified: 	2014/05/07
# Python Version: 	2.7

def no_odd(n):
	k = n
	odd = True
	while k > 0:
		if k%2 == 0:
			odd = False
			break
		else:
			k = k/10
	return odd

def solution035():
	target = 1000000
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	
	prime_numbers.insert(0,None)
	prime_numbers[1] = None

	count_circular = 0
	for p in range(len(prime_numbers)):
		if (prime_numbers[p] != None) and ((no_odd(p) == True) or p == 2):
			magnitude = len(str(p))
			circular = True
			new_p = p
			for i in range(magnitude):
				last = new_p%10
				new_p = last*10**(magnitude-1)+(new_p/10)
				if prime_numbers[new_p] == None:
					circular = False
			if circular == True:
				count_circular += 1
	
	return count_circular

print solution035()
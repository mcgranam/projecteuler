#!/usr/bin/env python

# File name: 		projecteuler046.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/16
# Date Modified: 	2014/05/16
# Python Version: 	2.7

def primes_list(n):
	target = n
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.insert(0,None)
	prime_numbers[1] = None
	return prime_numbers

def solution046():
	target = 2*10**5
	primes = primes_list(target)
	n = 3
	conjecture = True
	while conjecture == True:
		if primes[n] == None:
			p_list = filter(None,primes[0:n])
			conjecture = False
			for p in p_list:
				if ((n - p)/2)**0.5 == int(((n - p)/2)**0.5):
					conjecture = True
					break
			if conjecture == False:
				return n
		n += 2

print solution046()

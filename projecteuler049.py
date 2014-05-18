#!/usr/bin/env python

# File name: 		projecteuler049.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/18
# Date Modified: 	2014/05/18
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


def solution049():
	prime_list = primes(10000)

	for i in range(1000, len(prime_list)):
		if prime_list[i] != None:
			for n in range(1,(10000-i)/2):
				a = list(str(i))
				b = list(str(i+n))
				c = list(str(i+2*n))
				a.sort()
				b.sort()
				c.sort()
				a = ''.join(a)
				b = ''.join(b)
				c = ''.join(c)
				if (prime_list[(i+n)] != None) and (a == b):
					if (prime_list[(i+2*n)] != None) and (a == c):
						if i != 1487:
							return str(i)+str(i+n)+str(i+2*n)

print solution049()


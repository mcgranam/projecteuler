#!/usr/bin/env python

# File name: 		projecteuler047.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/17
# Date Modified: 	2014/05/17
# Python Version: 	2.7

def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def solution047():
	flag = False
	n = 0
	c = 0
	while flag == False:
		n += 1
		factors = list(set(prime_factors(n)))
		if len(factors) == 4:
			c += 1
		else:
			c = 0
		if c == 4:
			flag = True

	return n-3

print solution047()
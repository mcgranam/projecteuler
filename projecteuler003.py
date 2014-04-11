#!/usr/bin/env python

# File name: 		projecteuler003.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/11
# Date Modified: 	2014/04/11
# Python Version: 	2.7

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def solution003():
	target = 600851475143
	primes = prime_factors(target)
	return max(primes)

print solution003()

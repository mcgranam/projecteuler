#!/usr/bin/env python

# File name: 		projecteuler005.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/17
# Date Modified: 	2014/04/17
# Python Version: 	2.7

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# The smallest postive number that is even evenly divisibly is the number that has all of the same prime factors (including repeats) for the numbers 1-20.

def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

def solution005():
	target = 20
	prime_factors = []
	
	for i in primes_sieve(target):
		j = i
		prime_factors.append(i)
		while j <= (target / i):
			prime_factors.append(i)
			j = j * i

	return reduce(lambda x, y: x*y, prime_factors)

print solution005()

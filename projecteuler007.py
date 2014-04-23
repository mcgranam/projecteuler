#!/usr/bin/env python

# File name: 		projecteuler003.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/11
# Date Modified: 	2014/04/11
# Python Version: 	2.7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

prime_10001 = primes_sieve(200000)

print prime_10001[10000]


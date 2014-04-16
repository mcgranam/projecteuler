#!/usr/bin/env python

# File name: 		projecteuler003.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/11
# Date Modified: 	2014/04/11
# Python Version: 	2.7

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
	r = list(str(n))
	s = list(str(n))
	s.reverse()
	if s == r:
		return True

def solution004():
	max_palindrome = 0
	for i in range(100,1000):
		for j in range(100,1000):
			p = i*j
			if is_palindrome(p) and p > max_palindrome:
				max_palindrome = p
	return max_palindrome

print solution004()
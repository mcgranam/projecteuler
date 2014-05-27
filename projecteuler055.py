#!/usr/bin/env python

# File name: 		projecteuler005.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/27
# Date Modified: 	2014/05/27
# Python Version: 	2.7

def reverse(n):
	m = list(str(n))
	m.reverse()
	m = int(''.join(m))
	return m

def is_palendrome(n):
	m = list(str(n))
	m.reverse()
	m = int(''.join(m))
	if n == m:
		return True
	return False

def solution055():
	lychrel = 0
	for n in range(1,10000+1):
		is_lychrel = False
		for i in range(50):
			m = reverse(n)
			sum_chain = n + m
			if is_palendrome(sum_chain):
				is_lychrel = True
				break
			n = sum_chain
		if is_lychrel == False:
			lychrel += 1
	return lychrel

print solution055()
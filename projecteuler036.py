#!/usr/bin/env python

# File name: 		projecteuler036.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/09
# Date Modified: 	2014/05/09
# Python Version: 	2.7
import time
def palendrome(n):
	mag = len(str(n))
	k = n
	f = n%(10**mag)
	while k > 0:
		if f/(10**(mag-1)) != k%10:
			return False
		mag = mag-1
		k = k/10
		f = n%(10**mag)
	return True
	
target = 1000000

sum_palendromes = 0
for i in range(1,target+1,2):
	base10 = i
	base2 = int(bin(base10)[2:])
	if palendrome(base10) and palendrome(base2):
		sum_palendromes += base10

print sum_palendromes
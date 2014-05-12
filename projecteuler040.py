#!/usr/bin/env python

# File name: 		projecteuler040.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/12
# Date Modified: 	2014/05/12
# Python Version: 	2.7

def solution040():

	target_dec = 10**6
	dec = ''
	count = 1
	while len(dec) < target_dec:
		dec = dec + str(count)
		count += 1

	product = 1
	for i in range(7):
		product = product * int(dec[10**(i)-1])
	return product

print solution040()
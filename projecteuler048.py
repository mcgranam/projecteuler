#!/usr/bin/env python

# File name: 		projecteuler048.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/17
# Date Modified: 	2014/05/17
# Python Version: 	2.7

def solution048():
	power_sum = 0
	target = 1000
	for i in range(1,target+1):
		power_sum += i**i
	return str(power_sum)[-10:]

print solution048()
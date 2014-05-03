#!/usr/bin/env python

# File name: 		projecteuler025.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/03
# Date Modified: 	2014/05/03
# Python Version: 	2.7

# What is the first term in the Fibonacci sequence to contain 1000 digits?

def solution025():
	target_length = 1000
	f1 = 1
	f2 = 1
	count = 2
	while len(str(f2)) != target_length:
		f1, f2 = f2, f1+f2
		count += 1

	return count

print solution025()
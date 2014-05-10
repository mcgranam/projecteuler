#!/usr/bin/env python

# File name: 		projecteuler016.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/25
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

def solution016():
	base = 2
	exp = 1000

	return sum(map(int,(str(base**exp))))

print solution016()

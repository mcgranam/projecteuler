#!/usr/bin/env python

# File name: 		projecteuler033.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/08
# Date Modified: 	2014/05/08
# Python Version: 	2.7


def solution033():
	product = 1

	for i in range(11,99):
		for k in range(i+1,100):
			if (i%10 != 0) and (k%10 != 0):
				i_a = i/10*1.0
				i_b = i%10*1.0
				k_a = k/10*1.0
				k_b = k%10*1.0

				target = 1.0*i/k

				if (i_b == k_b) and (i_a/k_a == target):
					product = product * i_a/k_a
				if (i_b == k_a) and i_a/k_b == target:
					product = product * i_a/k_b
				if (i_a == k_b) and i_b/k_a == target:
					product = product * i_b/k_a
				if (i_a == k_a) and i_b/k_b == target:
					product = product * i_b/k_b

	# This will not always find the LCD
	return int(1/product)

print solution033()
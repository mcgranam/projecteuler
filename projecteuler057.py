#!/usr/bin/env python

# File name: 		projecteuler057.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/28
# Date Modified: 	2014/05/28
# Python Version: 	2.7

def solution057():
	expansion = 0
	count = 0
	num_nm1 = 1
	num_n = 3
	dem_n = 2
	while expansion < 1000:
		dem_np1 = num_n + dem_n
		num_np1 = 2*num_n + num_nm1
		num_nm1 = num_n
		dem_n = dem_np1
		num_n = num_np1

		if len(str(num_n)) > len(str(dem_n)):
			count += 1
		expansion += 1

	return count

print solution057()
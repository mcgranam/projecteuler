#!/usr/bin/env python

# File name: 		projecteuler044.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/14
# Date Modified: 	2014/05/14
# Python Version: 	2.7

# Not robust...
# Upper limit expliticly defined,
# Returns first value, which happens to be correct

def solution044():
	max_pent = 10**8
	pent_nums = [None]*max_pent

	n = 1
	c = 1
	while n < len(pent_nums):
		pent_nums[n] = n
		c += 1
		n = c*(3*c-1)/2

	pent_nums2 = filter(None,pent_nums)

	index = 0
	for i in pent_nums2:
		jndex = 0
		for j in pent_nums2[:index]:
			pent_i = pent_nums2[index]
			pent_j = pent_nums2[jndex]
			pent_ipj = pent_i + pent_j
			pent_imj = pent_i - pent_j
			if (pent_ipj == pent_nums[pent_ipj]) and (pent_imj == pent_nums[pent_imj]):
				return i-j
			jndex += 1
		index +=1

print solution044()
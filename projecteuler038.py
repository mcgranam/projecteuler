#!/usr/bin/env python

# File name: 		projecteuler038.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/10
# Date Modified: 	2014/05/10
# Python Version: 	2.7

def solution038():
	int_list = []
	max_num = 10000
	for i in range(1,max_num):
		if (str(i)[0] == "9"):
			int_list.append(i)

	max_cat_product = 192384576 # given
	for i in int_list:
		cat_product = ""
		n = 1
		while len(str(cat_product)) < 9:
			cat_product = cat_product + str(n*i)
			sorted_prod = list(cat_product)
			sorted_prod.sort()
			sorted_prod = "".join(sorted_prod)
			n += 1
		if sorted_prod == "123456789":
			if int(cat_product) > max_cat_product:
				max_cat_product = int(cat_product)

	return max_cat_product

print solution038()
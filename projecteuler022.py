#!/usr/bin/env python

# File name: 		projecteuler022.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/01
# Date Modified: 	2014/05/01
# Python Version: 	2.7

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

def solution022():

	f = open("projecteuler022.txt",'r')
	names = f.readline()
	name_list = names.split(',')
	clean_names = []
	for n in name_list:
		n = n[1:-1]
		clean_names.append(n)

	clean_names.sort()

	total_alpha_score = 0
	for c in range(len(clean_names)):
		alpha_score = 0
		for char in clean_names[c]:
			alpha_score += (ord(char) - 64)
		name_score = alpha_score * (c+1)
		total_alpha_score += name_score

	return total_alpha_score

print solution022()

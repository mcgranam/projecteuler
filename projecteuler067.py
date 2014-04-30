#!/usr/bin/env python

# File name: 		projecteuler067.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/25
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

f = open('projecteuler067.txt','r')
pyramid = f.readlines()
int_pyramid = []
for p in pyramid:
	row = p.strip()
	row = row.split(' ')
	row = map(int,row)
	int_pyramid.append(row)

size = len(int_pyramid)
for i in range(2,size+1):
	for j in range(len(int_pyramid[size-i])):
		max_step = + max(int_pyramid[size-i+1][j],int_pyramid[size-i+1][j+1])
		int_pyramid[size-i][j] = int_pyramid[size-i][j] + max_step
print int_pyramid[0][0]




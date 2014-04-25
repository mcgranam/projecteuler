#!/usr/bin/env python

# File name: 		projecteuler015.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/25
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# ￼
# How many such routes are there through a 20x20 grid?

size = 21
matrix = []
for a in range(size):
	for b in range(size):
		row = [0]*size
	matrix.append(row)

matrix[0][0] = 1
size = len(matrix)
for x in range(size):
	for y in range(size):
		if y == 0:
			matrix[y][x] = matrix[y][x] = 1
		elif x == 0:
			matrix[y][x] = matrix[y][x] = 1
		else:
			matrix[y][x] = matrix[y-1][x] + matrix[y][x-1]

for i in matrix:
	print i

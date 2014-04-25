#!/usr/bin/env python

# File name: 		projecteuler013.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/24
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def solution013():

	# Read numbers into python as a list
	f = open('projecteuler013.txt', 'r')
	number_list = f.readlines()
	number_sum = [0]*50
	for line in number_list:
		number = list(line.strip())
		for i in reversed(range(len(number))):
			n = int(number[i])

			# Add columns of numbers, ignoring base-10 representation
			number_sum[i] = number_sum[i] + n

	# Digit-wise addition, starting at the base of the number, turning the number into base 10, except for the leading digit.
	for i in reversed(range(len(number_sum))):
		if number_sum[i] > 9 and i > 0:
			number_sum[i-1] += number_sum[i]/10
			number_sum[i] = number_sum[i]%10

	# Turn string of numbers into integer, then take the 10 leading digits of that number
	s = map(str, number_sum)
	s = ''.join(s)
	s = int(s)
	while len(str(s)) > 10:
		s /= 10
	return s
		
print solution013()


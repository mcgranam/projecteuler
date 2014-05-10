#!/usr/bin/env python

# File name: 		projecteuler014.py
# Author: 		Matt McGranaghan
# Date Created:		2014/04/24
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def solution014():
	target = 1000000
	chain_lengths = []
	
	for n in range(1,target+1):
		i = n
		length = 1
		while i != 1:
			if i % 2 == 0:
				i = i/2
			else:
				i = 3*i+1
			
			if i <= len(chain_lengths):
				length += chain_lengths[i-1]
				break
			else:
				length +=1 

		chain_lengths.append(length)


	longest_chain = max(chain_lengths)
	starting_num  = chain_lengths.index(longest_chain)+1
	
	return starting_num

print solution014()

#!/usr/bin/env python

# File name: 		projecteuler042.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/13
# Date Modified: 	2014/05/13
# Python Version: 	2.7

def solution042():

	f = open('projecteuler042.txt', 'r')
	raw_data = f.readline()
	words = raw_data.replace("'","")
	words_list = words.split(",")

	tri_numbers = []
	tri_count = 0
	for i in range(1,50):
		tri_count +=i
		tri_numbers.append(tri_count)

	tri_scores = 0
	base = 64
	for w in words_list:
		word = w[1:-1]
		word_score = 0
		for char in word:
			word_score += ord(char) - base
		if word_score in tri_numbers:
			tri_scores += 1

	return tri_scores
			
print solution042()







#!/usr/bin/env python

# File name: 		projecteuler017.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/25
# Date Modified: 	2014/04/25
# Python Version: 	2.7

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def solution017():
	target = 6666
	letter_count = 0

	numbers = 	["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	thousands = ["thousand"]

	for i in range(1,target+1):

		word = []

		start_count = letter_count

		m = i / 1000
		if m > 0:
			letter_count += len(numbers[m-1])
			letter_count += len("thousand")
			word.append(numbers[m-1])
			word.append(thousands[0])

		h = (i % 1000)/100
		if h > 0:
			letter_count += len(numbers[h-1])
			letter_count += len("hundred")
			word.append(numbers[h-1])
			word.append("hundred")
			if h*100 != i:
				letter_count += len("and")
				word.append("and")

		t = (i % 100)/10
		if t > 1:
			letter_count += len(tens[t-2])
			word.append(tens[t-2])
		if t == 1:
			letter_count += len(numbers[9+(i%10)])
			word.append(numbers[9+(i%10)])

		d = i % 10 
		if d > 0 and t != 1:
			 letter_count += len(numbers[d-1])
			 word.append(numbers[d-1])

		# Just for fun
		# print " ".join(word)

	return letter_count

print solution017()


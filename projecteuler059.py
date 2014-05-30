#!/usr/bin/env python

# File name: 		projecteuler059.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/30
# Date Modified: 	2014/05/30
# Python Version: 	2.7

import operator

f = open('projecteuler059.txt','r')
coded_message = f.readline()
coded_message = coded_message.split(',')
for c in range(len(coded_message)):
	coded_message[c] = int(coded_message[c])

def solution059():
	max_decoded = 0
	for a in range(97,123):
		for b in range(97,123):
			for c in range(97,123):
				password = [a,b,c]
				decoded_char_count = 0
				decoded_message = []
				for char in range(len(coded_message)):
					cycle = char%3
					decoded_char = operator.xor(password[cycle],coded_message[char])
					if (decoded_char in range(65,90)) or (decoded_char in range(97,123)) or (decoded_char == 32):
						decoded_char_count += 1
					decoded_message.append(decoded_char)
					
				percent_decoded = decoded_char_count*1.0/len(decoded_message)
				if percent_decoded > max_decoded:
					print str(chr(a)) + str(chr(b)) + str(chr(c)), percent_decoded
					max_decoded = percent_decoded
				if percent_decoded > 0.95:
					print "password: ", str(chr(a)) + str(chr(b)) + str(chr(c))
					ascii_sum = 0
					for char in range(len(coded_message)):
						cycle = char%3
						decoded_char = operator.xor(password[cycle],coded_message[char])
						ascii_sum += decoded_char
					return ascii_sum

print solution059()
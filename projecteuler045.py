#!/usr/bin/env python

# File name: 		projecteuler045.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/15
# Date Modified: 	2014/05/15
# Python Version: 	2.7

def solution045():
	found = False
	n = 144
	a_t, b_t = (0.5),(0.5)
	a_p, b_p = (1.5),(-.5)
	while found == False:
		hexi = n*(2*n-1)
		c_p = -1*hexi
		quad_p = (-b_p + (b_p**2 - 4*a_p*c_p)**0.5)/(2*a_p)
		if quad_p == int(quad_p):
			c_t = -1*hexi
			quad_t = (-b_t + (b_t**2 - 4*a_t*c_t)**0.5)/(2*a_t)
			if quad_t == int(quad_t):
				return int(quad_t*(quad_t+1)/2)
		n += 1

print solution045()

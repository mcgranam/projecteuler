#!/usr/bin/env python

# File name: 		projecteuler043.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/13
# Date Modified: 	2014/05/13
# Python Version: 	2.7

import itertools
perms = [''.join(i) for i in itertools.permutations("0123456789")]

sum_special = 0
for p in perms:
	if int(p[1:4]) % 2 == 0:
		if int(p[2:5]) % 3 == 0:
			if int(p[3:6]) % 5 == 0:
				if int(p[4:7]) % 7 == 0:
					if int(p[5:8]) % 11 == 0:
						if int(p[6:9]) % 13 == 0:
							if int(p[7:10]) % 17 == 0:
								sum_special += int(p)

print sum_special




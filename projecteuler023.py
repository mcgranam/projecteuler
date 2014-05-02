
#!/usr/bin/env python

# File name: 		projecteuler023.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/01
# Date Modified: 	2014/05/01
# Python Version: 	2.7

def solution023():
	
	target = 28123
	abundent_numbers = []

	for n in range(1,target+1):
		divisors = []
		for i in range(1,int(n**0.5)+1):
			if n%i == 0:
				divisors.append(i)
				if (n/i != i) and (n/i != n):
					divisors.append(n/i)
		sum_divisors = sum(divisors)
		if sum_divisors > n:
			abundent_numbers.append(n)

	number_mesh = range(1,target+1)

	for x in range(len(abundent_numbers)):
		for y in range(x,len(abundent_numbers)):
			a = abundent_numbers[x]
			b = abundent_numbers[y]
			if a+b <= target:
				number_mesh[a+b-1] = None

	number_mesh = filter(None,number_mesh)

	return sum(number_mesh)

print solution023()
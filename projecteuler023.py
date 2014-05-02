
#!/usr/bin/env python

# File name: 		projecteuler023.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/01
# Date Modified: 	2014/05/01
# Python Version: 	2.7

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

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
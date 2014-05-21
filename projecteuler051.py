import itertools

def primes(target):
	prime_numbers = range(1,target+1)
	for p in range(2,target):
		if prime_numbers[p-1] != None:
			for i in range(p,target/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.pop(0)
	prime_numbers.insert(0,None)
	prime_numbers.insert(1,None)
	return prime_numbers

def replaceable_digits():
	perm_list = ['1','12','123','1234','12345','123456']
	replace_list = []
	for perm in perm_list:
		perms = itertools.permutations(perm)
		for p in perms:
			c = [int(p[0])]
			for i in p:
				if int(i) > c[-1]:
					c.append(int(i))
			if c not in replace_list:
				replace_list.append(c)
	return replace_list

prime_list = primes(1000000)
replace_list = replaceable_digits()

# for each replacement possibility, go through the original prime list and delete those digits.
# then look through what is left of the primes and see if there is 8 of any. 


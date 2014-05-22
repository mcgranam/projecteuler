import itertools
import copy

def primes(max_prime):
	prime_numbers = range(1,max_prime+1)
	for p in range(2,max_prime):
		if prime_numbers[p-1] != None:
			for i in range(p,max_prime/p+1):
				k = p*i		
				prime_numbers[k-1] = None
	prime_numbers.pop(0)
	prime_numbers.insert(0,None)
	prime_numbers.insert(1,None)
	return prime_numbers

def replaceable_digits(n):
	perm_list = []
	perm = ""
	for i in range(1,n):
		perm = perm+str(i)
		perm_list.append(perm)

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

def new_primes(prime_list,i_list):
	new_primes_list = []
	i_list.reverse()
	for p in prime_list:
		p = list(str(p))
		for i in i_list:
			del p[i]
		new_primes_list.append(p)
	return new_primes_list

prime_list = primes(100000)
prime_numbers = []
for p in prime_list:
	if (p != None) and (p > 10000):
		prime_numbers.append(p)
replace_list = replaceable_digits(5)
for r in replace_list:
	print r
	new_p_list = new_primes(prime_numbers,r)
	for n in new_p_list:
		if new_p_list.count(n) == 7:
			print n,r
			break






# prime_numbers = []
# for p in prime_list:
# 	if p != None and len(str(p)) > 4:
# 		x = list(str(p))
# 		prime_numbers.append(x)

# replace_list = replaceable_digits(5)
# replace_list.sort(lambda x,y: cmp(len(x), len(y)))

# for r_list in replace_list:
# 	p_list = copy.deepcopy(prime_numbers)
# 	for p in p_list:
# 		r_list.reverse()
# 		for r in r_list:
# 			print r
# 			del p[r]





# for each replacement possibility, go through the original prime list and delete those digits.
# then look through what is left of the primes and see if there is 8 of any. 


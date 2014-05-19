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

def solution050():
	prime_list = primes(100)
	prime_numbers = filter(None,prime_list)
	max_sum = 0
	for i in range(len(prime_numbers)):
		max_sum_i = 0
		for j in range(i+1,len(prime_numbers)):
			print i,j
			if max_sum_i + prime_numbers[j] > prime_numbers[-1]:
				break
			max_sum_i += j
			if max_sum_i == prime_list[max_sum_i]:
				if max_sum_i > max_sum:
					max_sum = max_sum_i
	return max_sum

print solution050()


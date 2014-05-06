#!/usr/bin/env python

# File name: 		projecteuler031.py
# Author: 			Matt McGranaghan
# Date Created:		2014/05/06
# Date Modified: 	2014/05/06
# Python Version: 	2.7

# In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:

# How many different ways can 2 be made using any number of coins?

def sum_coins(coins, coin_values):
	coin_total = 0
	for i in range(len(coins)):
		coin_total += coins[i]*coin_values[i]
	return coin_total

def solution031():
	coin_values = [200,100,50,20,10,5,2,1]
	target = 200
	valid_partitions = 0

	for p200 in range(target/coin_values[0]+1):
		total = sum_coins([p200],coin_values)
		for p100 in range((target-total)/coin_values[1]+1):
			total = sum_coins([p200,p100],coin_values)
			for p50 in range((target-total)/coin_values[2]+1):
				total = sum_coins([p200,p100,p50],coin_values)
				for p20 in range((target-total)/coin_values[3]+1):
					total = sum_coins([p200,p100,p50,p20],coin_values)
					for p10 in range((target-total)/coin_values[4]+1):
						total = sum_coins([p200,p100,p50,p20,p10],coin_values)
						for p5 in range((target-total)/coin_values[5]+1):
							total = sum_coins([p200,p100,p50,p20,p10,p5],coin_values)
							for p2 in range((target-total)/coin_values[6]+1):
								total = sum_coins([p200,p100,p50,p20,p10,p5,p2],coin_values)
								for p1 in range((target-total)/coin_values[7]+1):
									coins = [p200,p100,p50,p20,p10,p5,p2,p1]
									if sum_coins(coins,coin_values) == target:
										valid_partitions += 1

	return valid_partitions

print solution031()
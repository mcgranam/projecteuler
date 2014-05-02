import itertools
import time

def solution024():

	target = 10**6
	perms = [''.join(i) for i in itertools.permutations("0123456789")]
	return perms[target-1]

print solution024()

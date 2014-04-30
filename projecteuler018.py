f = open('projecteuler018.txt','r')
pyramid = f.readlines()
int_pyramid = []
for p in pyramid:
	row = p.strip()
	row = row.split(' ')
	row = map(int,row)
	int_pyramid.append(row)

size = len(int_pyramid)
for i in range(2,size+1):
	for j in range(len(int_pyramid[size-i])):
		max_step = + max(int_pyramid[size-i+1][j],int_pyramid[size-i+1][j+1])
		int_pyramid[size-i][j] = int_pyramid[size-i][j] + max_step
print int_pyramid[0][0]




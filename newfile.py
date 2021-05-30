import random
b=[0,1]
print('\u001b[32m')
d=0
while True:
	d=d+1
	a = random.choice(b)
	c = random.choice(b)
	print(a,c,a,c,c,a,a,c,a,c,c,a,a,c,a,c,c,a,c,a,c,c,a,a,c,a,c,c,a,a,c,a,c,c)
	if d==10:
		break
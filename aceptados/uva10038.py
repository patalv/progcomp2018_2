#!/usr/bin/env python
import sys
lista=[]
for line in sys.stdin:
	li=[]
	for var in line.split():
		var=int(var)
		li.append(var)
	if len(li) == 1:
		li=int(li[0])
	lista.append(li)
aux=list(lista)
for i in aux:
	n=i[0]
	i.remove(i[0])
	fok=0
	num=list([])
	if n == 1:
		print('Jolly')
		continue
	if (n == 2):
		dif=i[0]-i[1]
		if (dif == 1) or (dif == -1):
			print('Jolly')
		else:
			print('Not jolly')
	for j in range(1,len(i)):
		if j == 1:
			a=i[0]-i[1]
			if a < 0:
				a=-a
			num.append(a)
			continue
		b=i[j-1]-i[j]
		if b < 0:
			b=-b
		num.append(b)
	num.sort()
	for h in range(1,len(num)):
		if (num[h-1] != num[h]-1) or (num[0] != 1):
			print('Not jolly')
			break
		if num[h-1] == num[h]-1:
			if h == len(num)-1:
				print('Jolly')
			continue

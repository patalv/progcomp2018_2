#!/usr/bin/env python
import sys
import bisect
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

#print lista
for i in lista:
	if i == 0:
		break
	if (type(i) is list) == True:
		i.sort()
		cost=0 
#		print i
#		print cost
		for j in range(len(i)-1):
			if (len(i) <= 1):
				break
			tmp = i[0]+i[1] 
			bisect.insort_left(i,tmp)
			cost = cost + tmp
			i.remove(i[0])
			i.remove(i[0])
#			print i
#			print cost
		print(cost)

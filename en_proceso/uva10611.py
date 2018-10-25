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
#print lista
aux[1].sort()
aux[3].sort()
grillchimp=int(aux[0])
boychimp=int(aux[2])
a=0
b=0
for i in aux[3]:
	small=list([])
	big=list([])
	for j in aux[1]:
		if j < i:
			small.append(j)
		if j > i:
			big.append(j)
	small.sort()
	big.sort()
#	print small
#	print big
	if len(small) == 0:
		a=str('X')
	else:
		a=small.pop()
	if len(big) == 0:
		b=str('X')
	else:
		b=big[0]
	print (a,b)


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
grill=int(aux[0])
boy=int(aux[2])
for i in aux[3]:
	ismall=bisect.bisect_left(aux[1],i)-1
	ibig=bisect.bisect_right(aux[1],i)
	if ibig >= len(aux[1]):
		print(str(aux[1][ismall])+" "+ str('X'))
	elif ismall < 0:
		print(str('X')+" "+str(aux[1][ibig]))
	else:
		print(str(aux[1][ismall])+" "+str(aux[1][ibig]))

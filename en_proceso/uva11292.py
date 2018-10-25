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
casos=list([])
#print lista
for i in lista:
	#print i,'narf'
	if (type(i) is list):
		if (i[0] == 0) and (i[1] == 0):
			break
		heads=int(i[0])
		#print (heads)
		knights=int(i[1])
		aux.remove(i)
		cortar=list([])
		kni=list([])
		poid=list([])
		for j in range(heads):
			cortar.append(aux[0])
			#print aux[0],'derp'
			aux.remove(aux[0])
		for n in range(knights):
			kni.append(aux[0])
			#print aux[0],'troz'
			aux.remove(aux[0])
		poid.append(cortar)
		poid.append(kni)
		casos.append(poid)
#print casos
for i in casos:
	yes=0
	coin=0
	su=list([])
	i[1].sort()
	i[0].sort()
	#print i[1]
	if (len(i[0]) > len(i[1])):
		print ('loowater is doomed!')
		continue
	for j in i[0]:
		if next == 1:
			break
		for n in i[1]:
			if n >= j:
				coin=coin+n
				i[1].remove(n)
				#print su
				yes=1
				break
			f=int(len(i[1])-1)
			if (n < j) and (n == i[1][f]):
				yes=2
				next = int(1)
				break
	if yes == 1:
		print (coin)
	elif yes == 2:
		print ('loowater is doomed!')

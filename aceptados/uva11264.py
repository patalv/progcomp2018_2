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
monedas=list()
for i in lista:
	if type(i) is list:
		i.sort()
		suma=0
		cont=0
		for j in range(len(i)-1):
			if suma+i[j] < i[j+1]:
				monedas.append(i[j])
				suma=suma+i[j]
				cont = cont + 1
#				print str(j)+" "+str(i[j])+" "+str(suma)
		print(cont+1)

#!/usr/bin/env python
import sys
lista=[]
out=[]
for line in sys.stdin:
	li=[]
	for var in line.split():
		var=int(var)
		li.append(var)
	if len(li) == 1:
		li=li[0]
	lista.append(li)
lista2=list(lista)
#print lista2
x=0
for a in lista:
	if (type(a) is int) == True:
		if a == 0:
			lista2.remove(a)
			continue
		i=int(a)
		caso=[]
		for h in range(i+2):
			#print h, lista2[0]
			caso.append(lista2[0])
			lista2.remove(lista2[0])
		#x=int(i)
		out.append(caso)
#print out
for caso in out:
	for b in caso:
		if (type(b) is int) == True:
			i = int(b)
			comp=list(caso[1])
			for h in range(2,i+2):
				if (caso[h][0] > comp[0]) and (caso[h][1] > comp[1]):
					print('NE')
				if (caso[h][0] < comp[0]) and (caso[h][1] > comp[1]):
					print('NO')
				if (caso[h][0] < comp[0]) and (caso[h][1] < comp[1]):
					print('SO')
				if (caso[h][0] > comp[0]) and (caso[h][1] < comp[1]):
					print('SE')
				if (caso[h][0] == comp[0]) or (caso[h][1] == comp[1]):
					print('divisa')

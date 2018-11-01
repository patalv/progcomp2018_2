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

casos = []
n_heads = 0
n_knights = 0
n = -1;
heads = []
knights = []
for j in lista:
	if type(j) is list:
		n = n+1
		heads = j[0]
		knights = j[1]
		if heads > 0 or knights > 0:
			casos.append( [ [],[] ])
	else:
		if heads > 0:
			casos[n][0].append(j)
			heads = heads - 1
		elif knights > 0:
			casos[n][1].append(j)
			knights = knights - 1
			
for caso in casos:
#	print caso
	price = 0
	fail = False
	if len(caso[0]) > len(caso[1]):
		print('Loowater is doomed!')
		continue
	caso[0].sort()
	caso[1].sort()
	while len(caso[0]) > 0:
		if caso[0][0] <= caso[1][0]:
			price = price + caso[1][0]
			caso[0].pop(0)
			caso[1].pop(0)
		else:
			caso[1].pop(0)
			if len(caso[0]) > len(caso[1]):
				print('Loowater is doomed!')
				fail = True
				break
	if not fail:			
		print(price)
		
		

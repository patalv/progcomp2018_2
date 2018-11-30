#!/usr/bin/env python
import sys
from itertools import permutations
lista=[]
for line in sys.stdin:
	li=[]
	for var in line.split():
		var=int(var)
		li.append(var)
	if len(li) == 1:
		li=int(li[0])
	lista.append(li)
casos=[]
i=[]
while i!=[0,0]:
	aux=list([])
	i=list(lista[0])
	lista.remove(lista[0])
	aux.append(i)
	for h in range(i[1]):
		aux.append(lista[0])
		lista.remove(lista[0])
	casos.append(aux)
#print casos
for i in casos:
	n=i[0][0]
	m=i[0][1]
	if n==0 and m==0:
		break
	if n!=0 and m==0:
		print(len(list(permutations(range(n)))))
		continue
	d=list(permutations(range(n)))
#	print d
	possible=len(d)
	no=0
	for h in d:
		for j in range(1,m+1):
			num1=i[j][0]
			num2=i[j][1]
			cond=i[j][2]
			cuenta=0
			flag=0
			for k in range(n):
				if flag==1:
					cuenta=cuenta+1
				if flag==2:
					break
				if h[k]==num1 or h[k]==num2:
					flag=flag+1
#			print h,h[k]
#			print cuenta, cond
#			print possible
			if cond>0:
				if cuenta>cond:
					possible=possible-1
					break
			if cond<0:
				if cuenta<-cond:
					possible=possible-1
					break
#			print i[j], h
		
	print(possible)

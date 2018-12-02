#!/usr/bin/env python
from sys import stdin
from itertools import combinations
flag=0
while True:
	linea=stdin.readline().split()
	k=int(linea[0])
	if k==0:
		break
	if flag==0:
		flag=flag+1
	else:
		print('')
	linea.remove(linea[0])
	l=list([])
	for i in range(k):
		l.append(int(linea[i]))
	d=list(combinations(l,6))
	for j in d:
		a=str(j[0])
		b=str(j[1])
		c=str(j[2])
		d=str(j[3])
		e=str(j[4])
		f=str(j[5])
		print(a+' '+b+' '+c+' '+d+' '+e+' '+f)

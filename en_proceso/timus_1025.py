#!/usr/bin/env python
import sys
n=[]
for line in sys.stdin:
	for var in line.split():
		n.append(int(var))
even=n[0]-1
total= (even/2)+1
minimos=[]
for i in range(len(n)):
	g=((n[i]-1)/2)+1
	if i !=0:
		minimos.append(g)
l=[]
for c in minimos:
	personas=c
	aux=list(minimos)
	aux.remove(c)
	h=1
	for g in aux:
		if h >= total:
			personas=personas+g
			h=h+1
		else:
			l.append(personas)
			personas=c
			h=1
			continue	
		print g
		
suma=l[0]
print l
for j in l:
	if j < suma:
		suma=j
print suma

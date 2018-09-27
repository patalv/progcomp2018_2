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
for a in lista:
	if (type(a) is int) == True:
		if a != 0:
			N=a
		elif a == 0:
			out.append('')
	elif (type(a) is list) == True:
		for i in range(1,N):
			if (a[i-1]-a[i]) > 1:
				print 'es menor', a[i-1], a[i]
				out.append('No')
				break
			elif i == (N-1):
				out.append('Yes')
				break
l=len(out)
del out[l-1]
del out[l-2]
for x in out:
	print(x)

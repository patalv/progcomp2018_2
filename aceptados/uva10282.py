#!/usr/bin/env python
import sys
derp={}
nom=list()
for line in sys.stdin:
	a=line.split()
	if len(a) == 0:
		continue
	elif len(a) == 1:
		for i in a:
			nom.append(i)
	else:
		derp[a[1]] = a[0]
for i in nom:
#	print i
	try :
		print(derp[i])
	except:
		print('eh')

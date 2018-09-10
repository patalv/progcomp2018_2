#!/usr/bin/env python
import sys
import math
numbers=[]
numbereverse=[]
for line in sys.stdin:
	for var in line.split():
		var=int(var)
		numbers.append(var)
for i in range(len(numbers)):
	numbereverse.append(numbers[len(numbers)-i-1])
#print numbers
#print numbereverse
for j in numbereverse:
	a=math.sqrt(j)
	print ("%.4f" %(a))


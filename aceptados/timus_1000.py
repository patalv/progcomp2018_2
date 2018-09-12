#!/usr/bin/env python
import sys
numbers=[]
for line in sys.stdin:
	for num in line.split():
		num=float(num)
		numbers.append(num)
sol= numbers[0] + numbers[1]
if sol-int(sol) == 0:
	sol=int(sol) 
print sol


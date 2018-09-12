#!/usr/bin/env python
import sys
su=0
for line in sys.stdin:
	for var in line.split():
		n=int(var)
derp=abs(n)
if derp == 1:
	su=1
elif derp == 0:
	su=1
else:
	if (derp % 2) != 0:
		troz=derp-1
		su=(troz+1)*(troz/2)+derp
	elif (derp % 2) == 0:
		su=(derp+1)*(derp/2)
if n != abs(n):
	su=su-1
	su=-su
print su

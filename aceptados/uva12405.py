#!/usr/bin/env python
import sys
from sys import stdin
casos=int(stdin.readline())
lista=[]
for i in range(casos):
	char=int(stdin.readline())
	campo=list(stdin.readline())
	campo.remove('\n')
	lista.append(char)
	lista.append(campo)
for i in range(casos):
	scarecrow=0
	k=0
	char=int(lista[0])
	lista.remove(lista[0])
	for j in range(char):#para cada caracter
		if k == 1:
			k=2
			scarecrow=scarecrow+1
			continue
		elif k==2:
			k=0
			continue
		elif (lista[0][j] == '.') and (k==0):
			if j == len(lista[0])-1:
				scarecrow=scarecrow+1
				continue 
			k=1
			continue
	lista.remove(lista[0])
	print('Case '+str(i+1)+': '+str(scarecrow))

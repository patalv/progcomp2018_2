#!/usr/bin/env python
from sys import stdin
T = int(stdin.readline())#numero de casos
for _ in range(T):
    n = int(stdin.readline())#numero de nieves
    Max = 0
    li = [-1] * 1000000# lista con 1000000 de -1
    st = 0
    for i in range(n):# i itera entre cantidad de snowflakes del caso
        inin = int(stdin.readline())#lee numero identificador de nieve
        if li[inin] >= st:# si el -1 en la posicion del identificador unico de snowflake es mayor que st
            st = li[inin] + 1# entonces st toma el valor de la posicion inin en la lista li, inicialmente es -1 asi que st=0 al principio
        li[inin] = i# luego li[inin] toma el valor de i
        Max = max(Max, i - st + 1)# toma el valor maximo entre su iteracion anterior y i-st+1
    print(Max)
#por lo que entendi usa max(Max,i-st+1) como un contador para cada snowflake diferente, ya que cuando inin se repite se queda con el valor anterior
#codigo descargado de http://codytseng.nctu.me/2017/10/12/UVA-11572-Unique-Snowflakes/

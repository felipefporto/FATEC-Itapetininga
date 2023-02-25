#Escreva  um  programa  que  gere  uma  lista  que  é  resultado  do  produto  de  duas  listas  L1  e L2. Mostre na tela as 3 listas.
from random import randint
lista_1 = []
lista_2 = []
lista_3 = []
for i in range(5):
  lista_1.append(randint(0,10))
  lista_2.append(randint(0,10))
for i in range(5):
  lista_3.append(lista_1[i]*lista_2[i])
  print(lista_1[i], " * ", lista_2[i], " = ", lista_3[i])

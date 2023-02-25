#Faça  um  programa  que  percorra  duas  listas  e  gere  uma  terceira  lista  SEM  os  elementos repetidos. Mostra na tela as 3 listas.
from random import randint
lista_A = []
lista_B = []
for i in range(5):
  lista_A.append(randint(0,10))
  lista_B.append(randint(0,10))
#Tamanho máx que a lista pode atingir
lista_D = lista_A[:]
lista_D.extend(lista_B)
#Lista sem repetições
lista_C = []
c = 0
for k in range(len(lista_D)):
  for c in range(0,len(lista_C),1):
    if lista_D[k] == lista_C[c]:
      break
    c += 1
  if c == len(lista_C):
      lista_C.append(lista_D[k])
print(lista_D)
print(lista_C)

#-----------------------------------------------------

lis_1 = []
lis_2 = []
for i in range(5):
  lis_1.append(randint(1,20))
  lis_2.append(randint(1,20))
lis_3 = []
for i in range(5):
  if (lis_1[i] not in lis_2) and (lis_1[i] not in lis_3):
    lis_3.append(lis_1[i])
for i in range(5):
  if (lis_2[i] not in lis_1) and (lis_2[i] not in lis_3):
    lis_3.append(lis_2[i])
print("-------------------------------------------------------------------------")
print(lis_1)
print(lis_2)
print(lis_3)

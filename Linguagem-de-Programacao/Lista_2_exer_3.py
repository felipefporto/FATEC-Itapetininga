#Depois  calcule  e  mostre  na  tela  a quantidade  de  números  perfeitos. Um  número  é perfeito  quando  ele  é  igual  a  soma  dos seus  divisores  excetuando  ele  próprio.  (Ex:  6  é  perfeito,  6  =  1  +  2  +  3,  que  são  seus divisores).
lista_A = []
lista_B = []
lisca_C = []
from random import randint
for i in range(5):
  #Faça  um  programa  que preencha  duas  listas,  lista  A  e  lista  B com  5  números  em  cada.
  lista_A.append(randint(0,10))
  lista_B.append(randint(11, 21))
  #Gere a lista C,  com  os  números  da  lista  A  e  lista  B.
  lista_C = lista_A + lista_B
for k in range(len(lista_C)):
  perf = 0
  for c in range(1,lista_C[k],1):
    if lista_C[k] % c == 0:
      perf += c
  if perf == lista_C[k]:
    print("O número",lista_C[k],"é perfeito.")
  else:
    print("O número",lista_C[k],"não é perfeito.")
print(lista_C)

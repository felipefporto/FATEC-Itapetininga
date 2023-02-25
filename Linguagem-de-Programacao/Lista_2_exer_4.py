#Faça um programa que preencha duas listas com 10 elementos em cada. 
#Depois percorra essas duas listas e gere uma terceira lista com os números que se repetem nas duas listas. Mostre as três listas na tela.
from random import randint
lista_A = []
lista_B = []
lista_C = []
for i in range(10):
  lista_A.append(randint(0,100))
  lista_B.append(randint(0,100))
  for c in range(len(lista_A)):
    if lista_A[i] == lista_B[c]:
      lista_C.append(lista_A[i])
print(lista_A)
print(lista_B)
print(lista_C)

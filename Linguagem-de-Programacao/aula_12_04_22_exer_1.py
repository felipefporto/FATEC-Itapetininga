import random
lista_A = []
lista_B = []
for i in range(5):
    n = random.randint(0,50)
    lista_A.append(n)
for i in range(10):
    n = random.randint(0,50)
    lista_B.append(n)
print('--- Lista A ---')
print(lista_A)
print('--- Lista B ---')
print(lista_B)

dife = []
for i in range(5):
    num = lista_A[i]
    if (num in lista_B) == False:
        dife.append(num)
for i in range(10):
    num = lista_B[i]
    if (num in lista_A) == False and (num in dife) == False:
        dife.append(num)
print('--- Numeros que não são comuns ---')
print(dife)
print('-----------------------')
#--------------------------------------
from random import randint
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
print(lis_1)
print(lis_2)
print(lis_3)

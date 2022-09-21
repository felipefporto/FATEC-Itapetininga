# gera uma lista de números aleatórios, encontra o menor número da lista e quantidade de números maiores que 10.
from random import randint
num=[]
for i in range(5):
  num.append(randint(1,20))
print(num)
menor = num[0]
qtd = 0
for i in range(5):
  if num[i] < menor:
    menor=num[i]
  if num[i] > 10:
    qtd = qtd + 1
print(menor)
print(qtd)

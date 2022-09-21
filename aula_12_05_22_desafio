#Exer aula
import random
from random import randint
matriz = []
media = []
for i in range(5):
  linha = []
  linha.append(input('Entre com o nome do aluno: '))
  for j in range(3):
    linha.append(random.uniform(0,10))
  matriz.append(linha)
for i in range(5):
  soma = 0
  for j in range(1,4,1):
    soma += matriz[i][j]
  media.append(soma/3)
for i in range(5):
  print(matriz[i][0], " - %.2f" %media[i])

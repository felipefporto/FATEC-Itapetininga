#Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.
from random import randint
matriz = []
for i in range(3):
  linha = []
  for j in range(3):
    linha.append(randint(0,100))
  matriz.append(linha)
sum_linha = 0
qual_linha = 0
for linha in matriz:
  if sum(linha) >= sum_linha:
    sum_linha = sum(linha)
    qual_linha = linha
for i in range(3):
  print(matriz[i])
print(sum_linha)
print(qual_linha)
print('----------------')
#-------------------------
mat = []
for i in range(3):
  linha = []
  for j in range(3):
    linha.append(randint(1,20))
  mat.append(linha)
for i in range(3):
  print(mat[i])
soma = []
for i in range(3):
  soma.append(sum(mat[i]))
maior = max(soma)
print(soma)
idx = soma.index(maior)
print('A maior linha é: ',  mat[idx])
print('A maior soma da maior linha: ', maior)

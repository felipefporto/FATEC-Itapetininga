#Faça um programa que preencha uma matriz 3 * 5 e depois calcule e mostre:
from random import randint
import statistics
matriz = []
for i in range(3):
  linha = []
  for j in range(5):
    linha.append(randint(0,10))
  matriz.append(linha)
for i in range(3):
  print(matriz[i])
print('---')
max = 0
#O maior elemento da matriz e em queal linha e coluna ele está armazenado (tem que guardar os indíces)
impar = []
primos = []
for i in range(3):
  for j in range(5):
    if max <= matriz[i][j]:
      max = matriz[i][j]
      pos_i = i
      pos_j = j
#A média dos números ímpares da matriz
    if matriz[i][j] % 1 == 0:
      impar.append(matriz[i][j])
#mostre na tela todos os números primos, se houver.
    cont = 0
    for k in range(1,matriz[i][j]+1,1):
      if matriz[i][j] % k == 0:
        cont += 1
    if cont == 2:
      primos.append(matriz[i][j])
print('O maior valor da matriz é',max,'e está na posição é i é',pos_i,'e j é', pos_j)
if sum(impar) > 0:
  print(f'A média dos números ímpares da matriz: %.2f' %statistics.mean(impar))
else:
  print('A média dos números ímpares da matriz: 0')
print(primos)

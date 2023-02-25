#Faça um programa que, leia uma matriz 4x3 com os números inteiros. Calcule e mostre na tela:
#Crie um ventor e armazene os números dessa matriz no vetor mostrando na tela o resultado
from random import randint
matriz = []
vetor = []
for i in range(4):
  linha = []
  for j in range(3):
    linha.append(randint(0,100))
  matriz.append(linha)
for i in range(4):
  print(matriz[i])
print('---')
soma_j = cont_5_15 = 0
#A soma dos números da 2ª coluna (índice 1)
for i in range(4):
  for j in range(3):
    if j == 1:
      soma_j += matriz[i][j]
#A quantidade de números maiores que 5 e menores que 15 armazenados na matriz
    if matriz[i][j] > 5 and matriz[i][j] < 15:
      cont_5_15 += 1
    vetor.append(matriz[i][j])
print('A soma dos números da 2ª coluna: ', soma_j)
#A média dos números da 3ª linha (índice 2)
media = sum(matriz[2])/3
print(f'A média dos números da 3ª linha: %.2f' %media)
print('A quantidade de números maiores que 5 e menores que 15: ', cont_5_15)
print(vetor)
print('------')
#-----------------------------
mat = []
for i in range(4):
  lin = []
  for j in range(3):
    lin.append(randint(0,20))
  mat.append(lin)
for i in range(4):
  print(mat[i])
media = soma = qtde = 0
lista = []
for i in range(4):
  for j in range(3):
    if i == 2:
      media += mat[i][j]
    if j == 1:
      soma += mat[i][j]
    if mat[i][j] > 5 and mat[i][j] < 15:
      qtde += 1
    lista.append(mat[i][j])
media = media/3
print('Média da 3ª linha: ', media)
print('Soma da 2ª coluna: ', soma)
print('Qtde entre 5 e 15: ', qtde)
print('O vetor: ', lista)

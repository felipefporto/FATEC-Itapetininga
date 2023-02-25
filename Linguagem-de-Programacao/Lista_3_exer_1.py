#Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, calculee mostrena tela:
from random import randint
matriz = []
for i in range(3):
  linha = []
  for j in range(5):
    linha.append(randint(0,100))
  matriz.append(linha)
for i in range(3):
  print(matriz[i])
menor_num = matriz[1][1]
soma_3 = 0
coluna = []
for i in range(3):
  for j in range(5):
#a) menor número da matriz;
    if matriz[i][j] <= menor_num:
      menor_num = matriz[i][j]
#b) soma dos números múltiplos de 3 da matriz;
    if matriz[i][j] % 3 == 0:
      soma_3 += matriz[i][j]
#c) maior número da 3ª coluna da matriz (índice 2);
    if j == 2:
      coluna.append(matriz[i][2])
#d) média dos números da matriz;
soma = 0
for i in range(3):      
  soma += sum(matriz[i])
soma = soma/(3*5)
print('O menor elemento da matriz é: ', menor_num)
print('A soma dos números múltiplos de 3 da matriz: ', soma_3)
print('O maior número da 3ª coluna da matriz: ', max(coluna))
print(f'A média dos números da matriz: %.2f' %soma)

#Escreva um  programa  que  preencha  uma  matriz 4 x 6 com  números  inteiros, calcule e mostrena tela:
import statistics
from random import randint
matriz = []
for i in range(4):
  lista = []
  for j in range(6):
    lista.append(randint(0,100))
  matriz.append(lista)
qtde_10_30 = soma_10_2 = soma_4 = media_3 =0
#a) A quantidade de números que estão no intervalo entre 10 e 30
for i in range(4):
  for j in range(6):
    if matriz[i][j] > 10 and matriz[i][j] < 30:
      qtde_10_30 += 1
#b) A soma dos números maiores que 10 e pares
    if matriz[i][j] > 10 and matriz[i][j] % 2 == 0:
      soma_10_2 += matriz[i][j]
#c)A soma dos números que estão na quarta coluna da matriz
    if j == 3:
      soma_4 += matriz[i][j]
for i in range(4):
  print(matriz[i])
print('----')
print('A quantidade de números que estão no intervalo entre 10 e 30: ', qtde_10_30)
print('A soma dos números maiores que 10 e pares: ', soma_10_2)
print('A soma dos números que estão na quarta coluna da matriz: ', soma_4)
#d)A média dos números da matriz que estão na terceira linha
print(f'A média dos números da matriz que estão na terceira linha: %.2f' %statistics.mean(matriz[2]))

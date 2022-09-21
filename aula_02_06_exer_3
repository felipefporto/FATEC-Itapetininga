from random import randint
def pares(matriz):
  soma_pares = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      #a quantidade de números pares da matriz;
      if matriz[i][j] % 2 == 0:
        soma_pares += 1
  return soma_pares
def diagonal(matriz):
  soma_diagonal = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      #a soma dos elementos diagonal principal da matriz
      if i == j:
        soma_diagonal += matriz[i][j]
  return soma_diagonal
def media(matriz):
  media = 0
  for i in range(len(matriz)):
    media += sum(matriz[i])
  #a média dos elementos da matriz
  media = media/(len(matriz)*len(matriz[0]))
  return media
#Faça um programa que preencha uma matriz de ordem 3x3 de elementos inteiros. Faça uma função para cada cálculo abaixo: 
matriz = []
matriz_linhas = int(input('Digite a quantidade de linhas: '))
matriz_colunas = int(input('Digite a quantidade de colunas: '))
for i in range(matriz_linhas):
  linha = []
  for j in range(matriz_colunas):
    linha.append(randint(0,30))
  matriz.append(linha)
for i in range(3):
  print(matriz[i])
print('----')  
#os resultados deverão ser impressos no programa principal.
soma_pares = pares(matriz)
soma_diagonal = diagonal(matriz)
media_ = media(matriz)
print('A quantidade de números pares é: ', soma_pares)
print('A soma dos elementos diagonal principal da matriz: ', soma_diagonal)
print(f'A média dos elementos da matriz: %.2f' %media_)

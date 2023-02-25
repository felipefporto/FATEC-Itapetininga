from random import randint
matriz = []
media = qtd = 0
for i in range(3):
  linha = []
  for j in range(4):
    linha.append(randint(1,20))
  matriz.append(linha)
  media = media + sum(linha)
media = media/12
for i in range(3):
  print(matriz[i])
for i in range(3):
  for j in range(4):
    if matriz[i][j] > media:
     qtd += 1
print('Média da matriz: ', media)
print('Quantidade de números maiores que a média: ', qtd)

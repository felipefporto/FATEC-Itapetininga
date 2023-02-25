from random import randint
matriz = []
pares = impar = 0
for i in range(2):
  linha = []
  for j in range(4):
    linha.append(randint(1,20))
  matriz.append(linha)
for i in range(2):
  print(matriz[i])
for i in range(2):
  for j in range(4):
    if matriz[i][j] % 2 == 0:
      pares += 1
    else:
      impar += matriz[i][j]
print('Quantidade de pares: ', pares)
print('Soma dos ímpares: ', impar)

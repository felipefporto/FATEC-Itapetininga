#Façam um progrmaa que preencha uma matriz 5x3, calcule e mostre:
from random import randint
matriz = []
for i in range(5):
  linha = []
  for j in range(3):
    linha.append(randint(0,100))
  matriz.append(linha)
print('-------')
for i in range(5):
  print(matriz[i])
print('-------')
#A média de números que estão armazenados na matriz
soma = []
media = 0
for i in range(5):
  soma.append(sum(matriz[i]))
media = sum(soma)/(5*3)
print(f'A média da matriz é: %.2f' %media)
#A quantidade de números da matriz que são múltiplos de 3
#A soma dos números que são pares e maiores que 10
contador_m3 = []
soma_par_m10 = []
for i in range(5):
  for j in range(3):
    if matriz[i][j] % 3 == 0:
      contador_m3.append(1)
    if matriz[i][j] % 2 == 0 and matriz[i][j] > 10:
      soma_par_m10.append(matriz[i][j])
print('A quantidade de números da matriz que são mútiplos de 3 é: ', sum(contador_m3))
print('A soma dos números que são pares e maiores que 10 é de: ', sum(soma_par_m10))
print('------------')
#-----------------------------------
mat = []
for i in range(5):
  linha = []
  for j in range(3):
    linha.append(randint(1,20))
  mat.append(linha)
for i in range(5):
  print(mat[i])
media = qtde = soma = 0
for i in range(5):
  for j in range(3):
    if mat[i][j] % 3 == 0:
      qtde += 1
    if mat[i][j] % 2 ==0 and mat[i][j] > 10:
      soma = mat[i][j]
    media += mat[i][j]
media = media/15
print('Qtde de múltiplo de 3: ', qtde)
print('Soma dos pares e maiores que 10: ', soma)
print(f'A média dos números da matriz: %.2f' %media)

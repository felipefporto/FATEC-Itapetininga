#Faça um programa que, leia uma matriz 5x2 com os números de telefones dos clientes, as linhas representam os clientes, as colunas representam os telefones. E uma lista de 5 elementos com os nomes dos clientes. Depois de preenchidos a lista e a matriz, deverá ser feito uma busca pelo nome do cliente, se o nome existir, deverá ser mostrado na tela, os telefones desse cliente.
from random import randint
lista_nomes = []
matriz_telefones = []
for i in range(5):
  lista_nomes.append('Cliente '+str(i+1))
  linha = []
  for j in range(2):
    linha.append(randint(1000000,2000000))
  matriz_telefones.append(linha)
print(lista_nomes)
for i in range(5):
  print(matriz_telefones[i])
busca = str(input('Qual nome você deseja procurar na lista? '))
if busca in lista_nomes:
  if True:
    print('Os telefones são: ', matriz_telefones[lista_nomes.index(busca)][0],'e', matriz_telefones[lista_nomes.index(busca)][1])
else:
  print('Nome não está na lista')
#-------------------------
print('--------------')
tel = []
nome = []
for i in range(5):
  nome.append(input('Nome: '))
  lin = []
  for j in range(2):
    lin.append(randint(10000000,20000000))
  tel.append(lin)
for i in range(5):
  print(nome[i],' - ', tel[i])
pesq = input('Digite um nome para buscar: ')
while pesq.upper() != "FIM":
  if pesq in nome:
    idx = nome.index(pesq)
    print(pesq,' - telefones:', tel[idx])
  else:
    print('NOme não foi encontrado')
  pesq = input('Digite um nome para busca: ')

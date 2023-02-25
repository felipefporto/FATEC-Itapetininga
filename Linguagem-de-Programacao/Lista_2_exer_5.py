#Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com o valor dos produtos. Calcule e mostre:
import statistics
produtos = []
valor = []
contador_menor_10 = 0
contator_maior_media = 0
for i in range(5):
  produtos.append(str(input('Digite o nome do produto: ')))
  valor.append(float(input('Digite o valor do produto: ')))
  if valor[i] < 10:
    contador_menor_10 += 1
#c. a quantidade de produtos que valor acima da média;
for c in range(5):
  if valor[c] > statistics.mean(valor):
    contator_maior_media += 1
#a. a quantidade de produtos que o valor é abaixo de 10 reais;
print('A quantidade de produto com valor abaixo de R$10.00 é: ', contador_menor_10)
#b. a média dos valores dos produtos;
print('A média do valor dos produtos é: ', statistics.mean(valor))
#c. a quantidade de produtos que valor acima da média;
print('A quantidade de produtos com o Valor acima da média é de: ', contator_maior_media)
#d. a maior valor e o nome do produto;
print('0 maior valor é: ', max(valor), ', e o produto é: ', produtos[valor.index(max(valor))])
#e. faça uma listagem que imprima na tela (Nome Vlr do produto)
listagem = []
for i in range(5):
  listagem.append(produtos[i]+" R$"+str(valor[i]))
print(listagem)

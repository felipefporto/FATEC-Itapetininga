#Faça um programa que receba 10 números inteiros e armazene numa lista. Calcule e mostre:
# A quantidade de números pares
# A soma dos números ímpares
# A quantidade de números entre 10 e 20 (inclusive)
# A média dos números da lista
import statistics
lista = []
pares = []
impares = []
contador = 0
for i in range(10):
  lista.append(int(input("Digite um número inteiro: ")))
for c in lista:
  if c % 2 == 0:
      pares.append(c)
  else:
      impares.append(c)
  if c >= 10 and c<= 20:
    contador += 1
print(f'A quantidade de números pares: {len(pares)}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')
print(f'A quantidade de números entre 10 e 20 são: {contador}')
print('A média dos números da lista é: ', statistics.mean(lista))

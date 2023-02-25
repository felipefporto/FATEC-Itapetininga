#Faça um programa que receba 10 números inteiros. Calcule o fatorial de cada número e mostre na tela.

for i in range(10):
  #o menor valor multiplciado pelo fatorial sempre sera 1
  fatorial = 1
  num = int(input("Digite um numero: "))
  c = 2
  while c <= num:
    #como o fatorial ja inicia em 1 entao a variavel c inicia em 2
    #5! = 1*2*3*4*5 = 120
    fatorial = fatorial*c
    c += 1
  print("Fatorial do numero eh: %i" %fatorial)

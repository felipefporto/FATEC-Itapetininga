#Calcule e mostre:
soma_multiplo_3 = 0
soma_pares = 0
media_pares = 0
cont_pares = 0
cont_primos = 0

for i in range(10):
  #Faça um programa que receba dez números inteiros.
  num = int(input("Digite um número inteiro: "))
  #A quantidade de números primos
  verificador_num_primo = 0
  for c in range(1,num+1,1):
    if num % c == 0:
      verificador_num_primo += 1
  if verificador_num_primo == 2:
    cont_primos += 1
  #A soma dos números múltiplos de 3
  if num % 3 == 0:
    soma_multiplo_3 += num
  #A média dos pares que são maiores que 20
  if num % 2 == 0 and num > 20:
    soma_pares += num
    cont_pares += 1
if cont_pares != 0:
  media_pares = soma_pares / cont_pares
print("A quantidade de números primos é %i" %cont_primos)
print("A soma dos números múltiplos de 3 é %i" %soma_multiplo_3)
print("A média dos pares que são maiores que 20 é %i" %media_pares)  

#Faça um programa que receba dez números inteiros. 
#Calcule e mostre:

num_primo = 0
soma_multiplos = 0
contador_multiplos = 0
media_multiplos = 0
soma_maior_10_menor_30 = 0
media_maior_10_menor_30 = 0
contador_soma_maior_10_menor_30 = 0
verificador_num_primo = 0
soma_multiplos = 0
soma_primos = 0

for i in range(10):
    num = int(input("Digite um número: "))
    verificador_num_primo = 0
    #A média dos números múltiplos de 3 que são maiores que 10
    if num % 3 == 0 and num > 10:
        soma_multiplos += num
        contador_multiplos += 1
    #A média dos números
    #que são maiores OU iguais a 10 E menores OU iguais a 30
    if num >= 10 and num <= 30:
        soma_maior_10_menor_30 += num
        contador_soma_maior_10_menor_30 += 1
    #A soma dos números primos
    for c in range(1,num+1,1):
      if num % c == 0:
        verificador_num_primo += 1
    if verificador_num_primo == 2:
      soma_primos += num
if contador_soma_maior_10_menor_30 != 0:         
  media_maior_10_menor_30 = soma_maior_10_menor_30 / contador_soma_maior_10_menor_30
if contador_multiplos != 0:        
  media_multiplos = soma_multiplos / contador_multiplos
print("A média dos múltiplos de 3 e maiores que 10 é %i" %media_multiplos)
print("A média dos >= a 10 e <= a 30 é %i" %media_maior_10_menor_30)
print("A soma dos números primos é %i" %soma_primos)

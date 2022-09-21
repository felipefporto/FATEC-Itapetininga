#EXER 1

#Escreva um programa que leia um conjunto de 10 números inteiros,
#calcule e mostre:

menor = 0
impares = 0
pares = 0
i = 0
maior_20 = 0
cont_maior20 = 0

for i in range(10):
    num = int(input("Digite um número:" ))
    # o menor número    
    if i == 1:
        menor = num
    if num < menor:
        menor = num
    # a média dos números maiores que 20
    if num > 20:
        maior_20 += num
        cont_maior20 += 1
    # a soma dos números pares E maiores que 10
    if num % 2 == 0 and num > 10:
        pares += num
    # qtde de números impares    
    if num % 2 != 0:
        impares += 1
media_maior_20 = maior_20 / cont_maior20    

print("A soma dos números pares e maiores que 10 é de %i" %pares)
print("O menor valor digitado é %i" %menor)
print("A quantidade de números impares é %i" %impares)
print("A média dos números maiores que 20 é %i" %media_maior_20)

#Calcule e mostre na tela:
i = 1
idade = 0
cont_20_a_40 = 0
maior_idade = 0
menor_idade = 0
media_idade = 0
cont_idade = 0
soma_idade = 0
#Faça um programa que receba várias idades. Para finalizar a entrada deve ser digitado idade zero ou negativa. 
print("Para sair do programa digite um numero negativo ou zero")
while i > 0:
  idade = int(input("Digite a sua idade: "))
  i = idade
  # A quantidade de pessoas que tem idade entre 20 e 40 anos
  if idade >= 20 and idade <= 40:
    cont_20_a_40 += 1
  if i == 1:
    maior_idade = menor_idade = idade
    i = 2
  # A maior idade
  if maior_idade < idade:
    maior_idade = idade
  # A menor idade
  if menor_idade >= idade and idade !=0:
    menor_idade = idade
  # A média das idades
  if idade > 0:
    soma_idade += idade
    cont_idade += 1
if cont_idade != 0:
  media_idade = soma_idade / cont_idade
print("A quantidade de pessoas entre 20 e 40 anos: %i" %cont_20_a_40)
print("A menor idade: %i" %menor_idade)
print("A maior idade: %i" %maior_idade)
print("A media das idades: %i" %media_idade) 

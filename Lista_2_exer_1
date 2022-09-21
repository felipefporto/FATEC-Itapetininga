#1) Escreva  um  programa  que  leia a  idade  de  10  pessoas  
#e  armazene-as  em  uma  lista. Calcule e mostre:
#c)a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
#d)a quantidade de pessoas com idade maior que a média
from random import randint
import statistics
idade = []
count_20_a_30 = 0
count_maior_media = 0
for i in range(10):
  idade.append(randint(0,120))
  #c)a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
  if idade[i] >= 20 and idade[i] <= 30:
    count_20_a_30 += 1
  #d)a quantidade de pessoas com idade maior que a média
  if idade[i] > statistics.mean(idade):
    count_maior_media += 1
#a)a menor idade
print('A menor idade é: ', min(idade))
#b)a média das idades
print('A média das idade é: ', statistics.mean(idade))
#c)
print('A quantidade de pessoas entre 20 e 30 anos é de: ', count_20_a_30)
#d)
print('A quantidade de pessoas com idade maior que a média é: ', count_maior_media)

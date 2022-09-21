#Em um campeonato de futebol existem cinco times e cada um 
#possui onze jogadores.

#Faça um programa que receba a idade, o peso e a altura de 
#cada um dos jogadores, calcule e mostre:
idade = 0
peso = 0
altura = 0
media_idade = 0
soma_idade = 0
qtde_pessoas = 0
media_altura = 0
soma_altura = 0
soma_peso_80 = 0
soma_peso = 0
for i in range(1,6,1):
    qtde_menor_de_idade = 0
    print("Time ", i)
    for c in range(1,12,1):
        nome = str(input("Digite o seu nome: "))
        idade = int(input("Digite a sua idade: "))
        peso = float(input("Digite o seu peso: "))
        altura = float(input("Digite a sua altura: "))
        if idade <= 0 and peso <= 0 and altura <= 0:
            print("Digite valores válidos!")
        else:
            # A quantidade de jogadores com idade inferior a 18 anos
            if idade < 18:
                qtde_menor_de_idade += 1
            soma_idade += idade
            qtde_pessoas += 1
            soma_altura += altura
            soma_peso += peso
            if peso > 80:
                soma_peso_80 += peso
    # A média das idades dos jogadores de cada time
    media_idade = soma_idade / qtde_pessoas
    print("A média das idades dos jogadores do Time",i," é de: ",media_idade)
# A média das alturas de todos os jogadores do campeonato
media_altura = soma_altura / qtde_pessoas
# A percentagem de jogadores com mais de 80 quilos entre todos
#os jogadores do campeonato
porcentagem = soma_peso_80 / soma_peso * 100
print("A média das idades dos jogadores de cada time: ", media_idade)
print("A média das alturas de todos os jogadores do campeonato", media_altura)
print("A percentagem de jogadores com mais de 80kg: ", porcentagem)

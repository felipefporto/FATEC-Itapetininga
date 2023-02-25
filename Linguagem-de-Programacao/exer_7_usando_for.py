media_altura = 0
soma_altura = 0
qtde_pessoas = 0
maior_idade = 0
idade = 0
altura = 0
maior_altura = 0
menor_idade = 0
for i in range(10):
    nome = str(input("Qual é o seu nome? :"))
    idade = int(input("Qual é a sua idade? "))
    altura = float(input("Qual é a sua altura? "))
    if idade >= 0 and altura > 0:
        if i == 0:
            maior_idade = idade
            menor_idade = idade
            maior_altura = altura
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade
        if altura > maior_altura:
            maior_altura = altura
        soma_altura += altura
        qtde_pessoas += 1
    else:
        print("Digite um valor válido")

media_altura = soma_altura / qtde_pessoas
print("A média das alturas é: %.2f" %media_altura)
print("A maior idade é %i" %maior_idade)
print("A menor idade é %i" %menor_idade)
print("A maior altura é %.2f" %maior_altura)

cont_otimo = 0 
cont_bom = 0
cont_regular = 0
soma_idade = 0
media_idade = 0
#receba a idade e a opinião de um número indeterminado de pessoas.
idade = int(input("Caso queria sair do programa digite 0\n Qual é a sua Idade? "))
#Para finalizar a entrada deve ser digitado uma idade negativa ou zero.
while idade != 0 or idade < 0:
  #Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme (3- ótimo;2- bom;1-regular)
  #receba a opinião de um número indeterminado de pessoas.
  if idade > 0:
    opcao =int(input("Você gostou do filme? Escolha uma das opções \n1 - Regular\n2 - Bom\n3 - Ótimo\nOpção:"))
    soma_idade += idade
    if opcao == 1:
      cont_regular += 1
    elif opcao == 2:
      cont_bom += 1
    elif opcao == 3:
      cont_otimo +=1
  else:
    print("Digite uma opção válida")
  #receba a idade.
  idade = int(input("Qual é a sua Idade? "))
# A quantidade de pessoas que responderam ótimo
# A quantidade de pessoas que responderam regular
# A quantidade de pessoas que responderam bom
# A média das idades das pessoas
media_idade = soma_idade / (cont_regular + cont_bom + cont_otimo)
print("%i pessoas acharam o filme regular" %cont_regular)
print("%i pessoas acharam o filme bom" %cont_bom)
print("%i pessoas acharam o filme ótimo" %cont_otimo)
print("A média das idades é de %.2f anos" %media_idade)

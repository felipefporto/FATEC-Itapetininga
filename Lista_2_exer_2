#Faça um programa que preencha uma lista com 10 cores diferentes. 
#Depois permita fazer uma  pesquisa  se  uma determinada cor existe armazenada na  lista,  
#se  existir  deve  ser impresso  na  tela a  cor  e  em  qual  posição  (índice)  
#esta  cor  está armazenada.  
#A pesquisa deve ser feita até que seja digitado FIM na cor a ser pesquisadana lista.
cores = []
busca = "cor"
for i in range(3):
  cores.append(str(input('Digite uma cor: ')))
while busca.upper() != "FIM":
  try:
    busca = str(input("Qual é a cor que você deseja procurar?"))
    print("A cor é ", cores[cores.index(busca)], "e está no índice ", cores.index(busca))
  except:
    if busca.upper() == "FIM":
      print("O programa será encerrado.")
    else:
      print("Cor não encontrada, tente outra")

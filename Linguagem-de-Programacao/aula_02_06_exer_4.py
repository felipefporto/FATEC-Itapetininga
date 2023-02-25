#Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.

def busca(name):
  while name.upper() != "FIM":
  # o nome do aluno;
    if name in nomes:
      return True
    else:
      return False
    name = str(input('Qual o nome que deseja procurar?: '))
#######################################
nomes = []
for i in range(10):
  nomes.append('Nome '+str(i+1))
#######################################    
name = str(input('Qual o nome que deseja procurar?: '))
busca(name)
#######################################
if busca(name):
  if True:
    print('True')
  else:
    print('False')

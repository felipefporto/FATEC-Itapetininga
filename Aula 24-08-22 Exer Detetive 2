print('Responda as perguntas abaixo com S ou N')

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

respostas = []

for pergunta in perguntas:
  respostas.append(input(pergunta).upper())

classificacao = []

for resposta in respostas:
  if respostas == 'S':
    classificacao += 1

if sum(classificacao) < 2:
  print('Inocente')
elif sum(classificacao) == 2:
  print('Suspeita')
elif sum(classificacao) >= 3 and sum(classificacao) <= 4:
  print('Cúmplice')
else:
  print('Assassino')

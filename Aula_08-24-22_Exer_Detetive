perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
resposta = []
for i in range(5):
  print(perguntas[i])
  ver = input('Responda com Sim ou Não: ')
  resposta.append(ver.upper())
print(resposta)
if resposta.count('SIM') < 2:
  print('INOCENTE')
elif resposta.count('SIM') == 2:
  print('SUSPEITO')
elif resposta.count('SIM') >= 3 and resposta.count('SIM') <=4:
  print('CUMPLICE')
else:
  print('CULPADO')

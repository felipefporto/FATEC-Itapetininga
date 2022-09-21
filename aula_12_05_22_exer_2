m = []
for i in range(10):
  linha = []
  linha.append(input('Digite o nome da pessoa ' +str(i+1)+': '))
  linha.append(int(input('Digite a idade de ' + linha[0]+': ')))
  m.append(linha)
menor = m[0][1] #procura pessoa mais nova
pos = 0
for i in range(10):
  if m[i][1] <  menor:
    menor = m[i][j]
    pos = i
for i in range(10):
  print(m[i])
print('A pessoa mais nova é', m[pos][0])
#----------------
print('---------')
from random import randint
m2 = []
for i in range(5):
  linha2 = []
  for j in range(5):
    linha2.append(randint(1,10))
  m2.append(linha2)
media2 = 0
l = len(m2)
c = len(m2[0])
for i in range(5):
  media2 += sum(m2[i])
media2 = media2/(l*c)
for i in range(5):
  print(m2[i])
print('A média da matriz: ', media2)

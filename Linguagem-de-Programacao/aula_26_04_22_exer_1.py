turma = []
for i in range(3):
  linha = []
  for j in range(5):
    linha.append(int(input('Digite sua nota: ')))
  turma.append(linha)
print(turma)

for i in range(len(turma)):
  print(turma[i])

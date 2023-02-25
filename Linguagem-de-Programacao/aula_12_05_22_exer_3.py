matriz = []
parar = False
while not(parar):
  linha = [0]*10
  matriz.append(linha)
  x = input('Deseja parar? (S/N)')
  if x == 'S' or x == 's':
    parar = True
print('A matriz possui %d linhas' %len(matriz))
print('A matriz possui %d colunas' %len(matriz[0]))

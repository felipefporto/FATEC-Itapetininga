onibus = [0]*41
print(onibus)
poltrona = int(input('Entre com número da poltrona(1-40): '))
while poltrona != 0:
  if poltrona > 0 and poltrona <= 40:
    if onibus[poltrona] == 0:
      onibus[poltrona] = 1
      print("Poltrona já foi reservada")
    else:
      print("Essa poltrona já foi ocupada")
  else:
    print("Número da poltrona inválida")
  poltrona = int(input('Entre com número da poltrona(1-40): '))
qtd1 = 0
for i in range(1,41):
  if onibus[i] == 1:
    qtd1 += 1
print("Quantidade de poltronas ocupadas: ", qtd1)
print("Quantidade de poltronas livres: ", 40-qtd1)
  

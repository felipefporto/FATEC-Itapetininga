for i in range (0, 5, 1):
  num = int(input("Digite um número: "))
  soma_imp = 0
  for j in range (1, num+1, 1):
    if j % 2 == 1:
      soma_imp += j
  print("A soma dos números impares é de: ", soma_imp)

verificador = 0
num = int(input("Digite um número: "))
for i in range(1,num,1):
  if num % i == 0:
    verificador = verificador + i
if (verificador == num):
  print("O número %i é perfeito" %num)

def primo(num):
  cont_div = 0
  for k in range(1,num+1):
    if num % k == 0:
      cont_div+=1
  if cont_div == 2:
    print(num, 'é primo')
  else:
    print(num, 'não é primo')
print('chamando a função')
n1 = int(input('Entre com o número: '))
primo(n1)

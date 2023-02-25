#Elabore um programa que implemente uma função que receba um argumento. A função retorna o valor de caractere P se seu argumento for positivo e N se for zero ou negativo.
arg = int(input('Digite um valor: '))
def f_arg(arg):
  if arg <= 0:
    print('N')
  else:
    print('P')
f_arg(arg)

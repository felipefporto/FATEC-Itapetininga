#Elabore um programa, que implemente uma função que receba 10 argumentos, e que efetue a multiplicação de todos os argumentos.
import numpy

def mult():
  resultado = numpy.prod(lista)
  print('A multiplicação dos elementos da lista é: ', resultado)
  return resultado
lista = []
for i in range(10):
  num = int(input('Digite um número para a lista: '))
  lista.append(num)
mult()

letras = ['a','b','c','d','e']
print(letras[4])
print(letras[-1])
print(letras[-5])
print('-----')
lista1 = ['0','1','2','3','4']
lista2 = ['5','6','7','8','9', '5']
lista3 = lista2 + lista1
print(lista3)
print(lista3.count('5'))
print('-----')
print(lista3)
lista3.pop()
lista3.pop(1)
lista3.remove('5')
print(lista3)
print('-----')
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)
print('-----')
print(lista2)
lista2.reverse()
print(lista2)
print('-----')
print(lista3)
print(sorted(lista3))
print(lista3)
print('-----')

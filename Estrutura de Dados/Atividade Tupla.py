#Exer1
print('---')
tupla = ('')
for i in range(15):
  tupla = ('x') + tupla[:]
print(tupla)
print('---')
#Exer2
a = ('1','2','3')
b = tuple()
b = a[::-1]
print(a)
print(b)
print('---')
#Exer3
t1 = tuple('a')
t2 = tuple('b')
t3 = tuple('c')
t4 = tuple()
t4 = t1[:] + t2[:] + t3[:]
print(t4)
print('---')
carros = ("gol")
print(isinstance(carros, tuple))
carros = ("gol",)
print(isinstance(carros, tuple))
carros = ("gol","palio",)
print(isinstance(carros, tuple))

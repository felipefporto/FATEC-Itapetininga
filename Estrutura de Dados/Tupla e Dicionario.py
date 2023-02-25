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
#Dicionario
dic = {'joao': 100,'maria': 150}
print(dic['joao'])
print(dic['maria'])
dic['maria'] = 220
print(dic['maria'])
dic['pedro'] = 10
print(dic)
d = dict(x=1,y=2)
print(d['x'])
print('---')
x = {'Joao': [1,2], 'Maria': [3,4]}
print(x)
x.clear()
print(x)
print('------ Usando o Copy ele tirá copiar a raiz, pois a referencia é a mesma, por isso que ele altera as chaves em X e Y ------')
x = {'Joao': [1,2], 'Maria': [3,4]}
y = x.copy()
x['Joao'] += [9]
y['Pedro'] = [5,6]
print('------------')
print(x)
print(y)
print('------ Se eu não usar o copy ele separa as raízes e não altera a mesma Chave ------')
xx = {'Joao': [1,2], 'Maria': [3,4]}
yy = {'Joao': [1,2], 'Maria': [3,4]}
xx['Joao'] += [9]
yy['Pedro'] = [5,6]
print('------------')
print(xx)
print(yy)
print('------------')
print(y.items())
print(y.keys())
print(y.popitem())
print('---')
z = {'a': 1, 'b': 2, 'c': 3}
print(z)
zz = {'z': 9, 'b': 7}
z.update(a=7, c='xxx')
print(z)
print('---')
for chave, valor in z.items():
  print('Chave: ', chave)
  print('Valor: ', valor,'\n')
print('---')

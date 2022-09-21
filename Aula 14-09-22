def calcJuros(c,i,t, tipo = 'simples'):
  tipo = tipo.lower()
  if tipo == 'simples':
    j = c*i*t
    return j
  else:
    m = c*(1+i)**t
    return m

#chamada para juros simples
valor = calcJuros(2000, 3, 0.03)

#chamada para juros composto
montante = calcJuros(2000, 3, 0.03, 'composto')

#mostrando valores
print('Juros Simples: ', valor)
print('Montante de Juros Composto: ', montante)
print('----------------')
#######################################

def saudacao(nomes):
  for nome in nomes:
    print('Seja bem-vindo(a)', nome)

alunos = ['Ana', 'Maria', 'João', 'Luiz']
saudacao(alunos)
print('----------------')
########################################

def f():
  return

def g():
  return '0i'

def h(nome):
  return '0i, '+nome+' !'

print(f())
print(g())
print(h('João'))
print('----------------')
###################

def coordenadas():
  return 170, 36
#uma variável
xy = coordenadas()
print(xy[0])
print(xy[1])
#duas variaveis
x,y = coordenadas()
print(x)
print(y)
print('----------------')
############################

def dpessoais():
  dados = ['Maria',23,'o+']
  return dados

nome, idade, sangue = dpessoais()
print(nome)
print(idade)
print(sangue)
print('----------------')
########################
#return tupla
def dados():
  return ('Maria', 23, 'o+', 'Paulo', 'Joana')

nome, idade, *_ = dados()
print(nome)
print(idade)
print('----------------')

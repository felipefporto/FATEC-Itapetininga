class Carro(object):
  pass
fusca = Carro()
fusca.estado = 'novo'
print(fusca.estado)
###################################
print('--------')
class Carro(object):
  estado = 'novo'
print(Carro.estado)
###################################
print('--------')
bmw = Carro()
print(bmw.estado)
###################################
print('--------')
class Carro(object):
  def dirigir(self):
    self.estado = 'usado'
bmw = Carro()
#print(bmw.estado) AtributeError: 'Carro' object has no attribute 'estado'
bmw.dirigir()
print(bmw.estado)
###################################
print('--------')
class Carro(object):
  estado = 'novo'
  def dirigir(self):
    self.estado = 'usado'
porsche = Carro()
porsche.dirigir() 
print(porsche.estado)
ferrari = Carro()
print(ferrari.estado)
###################################
print('--------')
class Carro(object):
  def __init__(self,estado):
    self.estado = estado
bmw = Carro('semi-novo')
print(bmw.estado)

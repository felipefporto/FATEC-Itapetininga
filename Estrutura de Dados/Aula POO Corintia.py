class Time():
  def __init__(self):
    pass
  def camp(self):
    print('BR22')
  def nome(self):
    print('UM TIME')
  def tradicao(self):
    print('TIME QUE GANHA TITULOS')
class Corinthians(Time):
  def nome(self):
    print('SCCP')
  def tradicao(self):
    print('BI MUNDIAL')
class Rival(Time):
  def nome(self):
    print('Não ganha títulos')
cor = Corinthians()
riv = Rival()
print('Cor: ')
cor.nome()
cor.camp()
cor.tradicao()
print('Riv: ')
riv.nome()
riv.camp()
riv.tradicao()

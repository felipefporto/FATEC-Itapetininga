#Crie uma classe Veiculo com o método construtor e com os seguintes atributos:
#modelo, cor, combustível, cambio, ano, preço e velocidade máxima
#No mesma codificação crie duas instancias da classe Veículos. OBS: Defina os valores dos atributos passando argumentos no método construtor e imprima-os

class Veiculo(object):
  def __init__(self, modelo, cor, combustivel, cambio, ano, preco, velocidade_max):
    self.modelo = modelo
    self.cor = cor
    self.combustivel = combustivel
    self.cambio = cambio
    self.ano = ano
    self.preco = preco
    self.velocidade_max = velocidade_max
    
fusca = Veiculo('Fusca', 'Preto', 'Gasolina', 'Manual', '1971', 'R$30.000,00', '180km/h')
gol = Veiculo('Gol', 'Azul', 'Flex', 'Manual', '2020', 'R$60.000,00', '230km/h')

print('-----')
print('Modelo: ', fusca.modelo, '\nCor: ', fusca.cor,'\nCombustível: ', fusca.combustivel,'\nCâmbio: ', fusca.cambio,'\nAno: ', fusca.ano,'\nPreço: ', fusca.preco,'\nVelocidade Máxima: ', fusca.velocidade_max)
print('-----')
print('Modelo: ', gol.modelo, '\nCor: ', gol.cor,'\nCombustível: ', gol.combustivel,'\nCâmbio: ', gol.cambio,'\nAno: ', gol.ano,'\nPreço: ', gol.preco,'\nVelocidade Máxima: ', gol.velocidade_max)
print('-----')

modelo = input('Digite qual o modelo do Carro: ')
cor = input('Digite qual é a Cor: ')
combustivel = input('Digite qual o combustível que é usado: ')
cambio = input('Digite qual o modelo do Câmbio: ')
ano = input('Digite qual o ano do carro: ')
preco = input('Digite qual o preço: ')
velocidade_max = input('Digite qual a velocidade máxima: ')

carrito = Veiculo(modelo, cor, combustivel, cambio, ano, preco, velocidade_max)

print('-----')
print('Modelo: ', carrito.modelo, '\nCor: ', carrito.cor,'\nCombustível: ', carrito.combustivel,'\nCâmbio: ', carrito.cambio,'\nAno: ', carrito.ano,'\nPreço: ', carrito.preco,'\nVelocidade Máxima: ', carrito.velocidade_max)

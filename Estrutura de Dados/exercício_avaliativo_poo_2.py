#Exercício 4:
#Crie uma classe Notebook com o método construtor e com os seguintes argumentos:
#Marca, modelo, memoria_ram, placa_video, processador e disco.
#Definir 4 métodos: Iniciar, Reiniciar, atualizar e informações;
#Por fim, chamar os métodos implementados.
class Notebook(object):
  def __init__(self, marca, modelo, memoria_ram, placa_video, processador, disco):
    self.marca = marca
    self.modelo = modelo
    self.memoria_ram = memoria_ram
    self.placa_video = placa_video
    self.processador = processador
    self.disco = disco
  def iniciar():
    print('Ligando o Notebook...')
  def reiniciar():
    print('Reinicialização necessária. Preparando para Reiniciar. \nReiniciando... \nTudo Pronto!')
  def atualizar():
    print('Você tem atualizações a serem instaladas! Preparando atualizações do SO...')
  def informações():
    print('Sistema Atualizado! \n--- Informações do Sistema ---')
    print('Marca: ', notebook.marca, '\nModelo: ', notebook.modelo,'\nMemória Ram: ', notebook.memoria_ram,'\nPlaca de Vídeo: ', notebook.placa_video,'\nProcessador: ', notebook.processador,'\nDisco: ', notebook.disco)
    
notebook = Notebook('Asus', 'ATX-2567', '16gb DDR4', 'GTX 3060', 'i7 11th', '500 ssd')

Notebook.iniciar()
Notebook.atualizar()
Notebook.reiniciar()
Notebook.informações()

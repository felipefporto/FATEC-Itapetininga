#Crie uma função recursiva que implemente fatorial de um número.

def f_fatorial(numero):
    if numero == 0: #BASE
      return 1
    else: #BASE RECURSIVA
      return numero*f_fatorial(numero-1)

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {f_fatorial(numero)}")

#Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente).
#Se o expoente for zero, a potência é igual 1 (critério de parada)
#Obs. Não considere exponenciação de números negativos

def f_potencia(base, expoente):
  if expoente == 0: #BASE
    return 1
  else: #BASE RECURSIVA
    return base*f_potencia(base, expoente-1)

base = int(input("Digite o valor da base "))
expoente = int(input("Digite o valor do expoente "))

if expoente <= 0:
  print("Não considere exponenciação de números negativos")
  expoente = int(input("Digite o novo valor POSITIVO do expoente "))
  
print(f"A potencia da {base} elevado ao expoente {expoente} é {f_potencia(base, expoente)}")

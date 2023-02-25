#Escreva um programa que preencha uma lista com os nomes de 5 vendedores, preencha também  outra  lista  com  valor  total  das  vendas  de  cada  vendedor.  Cada  vendedor recebe 10% de comissão sobre as vendas. Faça os seguintes cálculos e mostre os resultados na tela: 
import statistics
vendedor = []
venda_real = []
comissao = []
for i in range(5):
  vendedor.append(str(input('Digite o nome do vendedor: ')))
  venda_real.append(float(input('Digite o valor total das vendas: ')))
  comissao.append(0.1*venda_real[i])
  #a. Uma  listagem  com  o  nome  e  o  valor  a  receber  de  cada  vendedor  (total  das vendas * 0.10)
  print('O vendedor', vendedor[i], 'conseguiu R$', comissao[i],'de comissão')
  #b. O total (bruto) vendido pelos 5 vendedores
  print('O valor Bruto vendido pelo vendedor', vendedor[i], 'foi de R$', venda_real[i])
#c. A média do total de vendas (valor bruto vendido por cada vendedor)
print('A média total de vendas foi de R$', statistics.mean(venda_real))
#d. A quantidade de vendedores que venderam acima da média das vendas.
qtde_venda_acima_media = 0
for c in range(5):
  if venda_real[c] > statistics.mean(venda_real):
    qtde_venda_acima_media += 1
print('A quantidade de vendas acima da média de vendas foi de: ', qtde_venda_acima_media)
#e. O maior valor de comissão e o nome do vendedor que recebeu
print('O maior valor de comissão foi de', max(comissao), 'do vendedor', vendedor[comissao.index(max(comissao))])

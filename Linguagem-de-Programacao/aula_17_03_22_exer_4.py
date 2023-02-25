listaA = []
listaB = []
for i in range(10):
  listaA.append(float(input('Digite um número: ')))
  listaB.append(listaA[i]/2)
listaA.sort()
listaB.sort(reverse=True)
print('Ordem Crescente:', listaA)
print('Ordem Decrescente:', listaB)

def maior(vetor): #ordena o vetor e retorna o maior
  if len(vetor) > 1:
    for j in range(0,len(vetor)):
      for i in range(0,len(vetor)-1):
        if vetor[i] > vetor[i+1]:
          aux = vetor[i+1]
          vetor[i+1] = vetor[i]
          vetor[i] = aux
  return vetor[len(vetor)-1] #retorna o último elemento do vetor

v = [5, 4, 3, 2, 1]
print(v)
m = maior(v)
print(m)
print(v)

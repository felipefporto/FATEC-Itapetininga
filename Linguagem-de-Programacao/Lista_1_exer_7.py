#Faça um programa que calcule e mostre na tela a tabuada de 1 a 10.
m = 0
for i in range(1,11,1):
    for c in range(1,11,1):
        m = i * c
        print("",i," * ",c," = ",m)

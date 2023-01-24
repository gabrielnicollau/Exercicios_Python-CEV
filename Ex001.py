# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite o número para saber a sua tabuada: '))
print('\033[33m=-\033[m' * 8)

for tabuada in range(0, 11):
    calculo = numero * tabuada
    print('{} x {:2} = {}'.format(numero, tabuada, calculo))

print('\033[33m=-\033[m' * 8)
print('\033[31mFIM!\033[m')

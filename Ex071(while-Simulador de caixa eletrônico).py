"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

# Crie uma variável chamada "saque" que receba como parâmetro o valor a ser sacado.

# Valor a ser sacado
valor = int(input('Valor de saque: R$'))

total = valor  # dinheiro
cedula = 50  # Valor da primeira cédula.
quantCedula = 0
# Loop para subtrair o total de acordo o valor da cédula.

while True:  # Enquanto o total a ser sacado for maior ou igual o valor da célula, tirar 50 do total e contar 1 para cada subtração.
    if total >= cedula:
        total -= cedula
        quantCedula += 1

    else:  # Quando o total tiver o mesmo valor da cédula, no caso 50, mudar o valor dela.
        if quantCedula > 0:  # Verificar a quantidade de cédulas e imprimir para cédula se for possivel fazer a subtração.
            print(f'Você sacou {quantCedula} cédulas de {cedula} reais.')

# Se não for verdadeira a primeira condição.
# Essa condição só vai ser aceita quando o total virar Falso, no caso, tanto o valor do total quanto da cédula serem o mesmo.
        if cedula == 50:  # Se cédula for igual a 50.
            cedula = 20  # Mudar o valor dela

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        quantCedula = 0

        if total == 0:
            break
print()
print('OPERAÇÃO ENCERRADA!')
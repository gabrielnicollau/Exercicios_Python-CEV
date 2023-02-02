"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

extenso = ('Zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

# loop para o usuário digitar até aceitar o número de 0 até 20.
while True:
    numero = int(input('Extenso do número [0 até 20]: '))
    if 0 <= numero <= 20:  # Verificar se o número digitado do usuário está entre 0 e 20.
        print(f'O extenso do número {numero} é {extenso[numero]}.')
        break
    else:
        print('\033[31mNúmero inválido, tente novamente [0 até 20]...\033[m')
# Se usuário digitou 5, será substituido na posição 4, ou seja, cinco(posição 4), vai virar numero 5.

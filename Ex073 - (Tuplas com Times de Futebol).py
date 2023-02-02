"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros Times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o Time da Chapecoense.
"""

# Tabela de 2022.
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
         'São Paulo', 'América-MG', 'Botafogo', 'Santos'
         'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará-SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Lista de times do Brasileirão: {times}.')  # Mostrar a tupla.
print('=' * 30)
print(f'Os 5 primeiros são: {times[0:5]}.')  # Mostrar do objeto 0 até o objeto 5.
print('=' * 30)
print(f'Os 5 últimos são: {times[-4:]}.')  # Mostrar os últimos objetos de trás para frente.
print('=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}.')  # Motrar por ordem alfabética
print('=' * 30)
print(f'O São Paulo estpa na {times.index("São Paulo") + 1}ª.')  # +1 para mostrar o oitavo.

variavel = ['Gustavo', 'aJoaozinho', 'Maria']


comecaComJ = False

"""
for valor in variavel:
    if valor.lower().startswith('j'):
        comecaComJ = True

if comecaComJ:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')
"""

for valor in variavel:
    if valor.lower().startswith('j'):
        print('Existe uma palavra que começa com J')
        break
else:
    print('Não existe uma palavra que começa com J')
    # Serve para que quando termine o laço entre no else. Caso o laço seja breakado, o else não vai ser executado.

"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Curitiba']

# Código
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

for valor in cidades_estados:
    print(valor[0], valor[1])


estados_cidades = zip_longest(estados, cidades, fillvalue='Estado')
for valor in estados_cidades:
    print(valor[0], valor[1])

"""
# {'chave':'valor', 'chave2':'valor}
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'

del d1['chave1']


for k in d1:
    print(k)

for v in d1.values():
    print(v)

for i in d1.items():
    print(i)

for k, v in d1.items():
    print(k, v)
"""


clientes = {
    'cliente1': {
        'nome': 'Gustavo',
        'sobrenome': 'Gelinski',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


"""
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)

"""

"""
Formatando valores com modificadores

    :s - strings
    :d - inteiros
    :f - float
    :.(NUMERO)f - Quantidade de casas decimais float
    :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

    > - Esquerda
    < - Direita
    ^ - Centro
"""

num_1 = 1
print(f'{num_1:0^5}')


nome = 'gustavo gelinski'

print(nome.lower())
print(nome.upper())
print(nome.title())

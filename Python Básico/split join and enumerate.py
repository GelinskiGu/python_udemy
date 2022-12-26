"""

Split, Join, Enumerate
* Split - Dividir uma string
* Join - Juntar uma lista
* Enumerate - Enumerar elementos da lista

"""
"""
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista = string.split(' ')  # Separa tudo quando aparece o espaço em um array

for value in lista:
    print(value, lista.count(value))
"""
"""
string = 'O Brasil é penta.'
lista = string.split(' ')
# Interessante para transformar um array em uma string
string2 = ' '.join(lista)

print(string2)
"""

string = 'O Brasil é penta.'
lista = string.split(' ')

for index, value in enumerate(lista):
    print(index, value)

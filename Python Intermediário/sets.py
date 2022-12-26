# add, update, clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
# é iterável
"""
s1 = {1, 2, 3, 4, 5}

s1.add(6)

s1.discard(3)
"""
# bom para remover elementos duplicados de listas

l1 = [1, 2, 1, 1, 1, 1, 3, 4, 5, 6, 6, 6, 1, 2, 'Gustavo', 'Gustavo']
l1 = set(l1)

print(l1)

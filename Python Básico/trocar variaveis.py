# Padrão em toda linguagem:

from re import X


x = 10
y = 20

z = x
x = y
y = z


# Em python:

x = 10
y = 20

x, y = y, x

print(x, y)

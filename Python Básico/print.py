
print('Gustavo', 'Gelinski', sep='-', end='')
print('Gustavo', 'Gelinski', sep='.')  # sep é o separador de cada argumento.


print('824', '176', '070', sep='.', end='-')
print(18)

# r serve para não executar nada do que está no print
print(r'Esse e meu \n (str).')

nome = 'Gustavo Gelinski'
idade = 20
altura = 1.70
peso = 70
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

cpf = '10951060905'
cpf_array = []
soma = 0

for i in range(9):
    cpf_array.append(str(cpf[i]))
    soma += int(cpf_array[i]) * (10-i)

print(soma)
equacao = 11 - (soma % 11)

if (equacao > 9):
    digito1 = 0
else:
    digito1 = equacao

cpf_array.append(str(digito1))

soma = 0

for i in range(10):
    soma += int(cpf_array[i]) * (11-i)

equacao = 11 - (soma % 11)
digito2 = equacao

cpf_array.append(str(digito2))
cpf_string = ''.join(cpf_array)

if (cpf_string == cpf):
    print('CPF Válido.')
else:
    print('CPF Inválido.')

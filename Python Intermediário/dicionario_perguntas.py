perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '2', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    },
}

respostas_certas = 0
for chave_pergunta, valor_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valor_pergunta["pergunta"]}')
    for rk, rv in valor_pergunta['respostas'].items():
        print(f'\t{rk}) {rv}')

    resposta_usuario = input('Sua resposta:')

    if resposta_usuario == valor_pergunta['resposta_certa']:
        print('Resposta correta!')
        respostas_certas += 1

    else:
        print('Resposta incorreta.')

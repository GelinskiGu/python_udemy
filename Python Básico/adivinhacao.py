palavra_secreta = 'perfume'
letras_digitadas = []
letras_corretas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    else:
        letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'"{letra.upper()}" é uma letra correta.')
    else:
        print('Letra incorreta')
        letras_digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print(f'Você achou a palavra secreta que é {palavra_secreta}')
        break
    else:
        print(f'A palavra está assim: {secreto_temporario}')

    if letra not in palavra_secreta:
        chances -= 1

    print(f'Você ainda tem {chances} chances')

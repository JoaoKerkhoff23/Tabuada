import random
print('vamos jogar jokenpô!!')
play = 0
while play == 0:
    escolhas = ['pedra', 'papel', 'tesoura']
    esc = random.randint(1, 3)
    print('selecione sua opção!')
    print('[ 1 ] PEDRA')
    print('[ 2 ] PAPEL')
    print('[ 3 ] TESOURA')
    tent = int(input('escreva sua opção:'))
    print('-' * 10)
    print('o computador jogou {}'.format(escolhas[esc]))
    print('você jogou {}'.format(escolhas[tent]))
    print('-' * 10)
    if esc == 1:
        if tent == 1:
            print('empate')
        elif tent == 2:
            print('jogador venceu')
        elif tent == 3:
            print('computador venceu')
        else:
            print('jogada invalida')
        play = int(input('escreva 0 para jogar novamente ou 1 para parar'))
        print('obrigado por jogar!')
    elif esc == 2:
        if tent == 1:
            print('computador venceu')
        elif tent == 2:
            print('empate')
        elif tent == 3:
            print('jogador venceu')
        else:
            print('jogada invalida')
        play = int(input('escreva 0 para jogar novamente ou 1 para parar'))
        print('obrigado por jogar!')
    elif esc == 3:
        if tent == 1:
            print('jogador venceu')
        elif tent == 2:
            print('computador venceu')
        elif tent == 3:
            print('empate')
        else:
            print('jogada invalida')
        play = int(input('escreva 0 para jogar novamente ou 1 para parar'))
        print('obrigado por jogar!')
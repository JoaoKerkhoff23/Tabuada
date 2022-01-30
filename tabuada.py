from random import randint
play = 1
while play == 1:
    x = randint(0,11)
    y = randint(0,11)
    print('a multiplicação de{}x{}'.format(x,y))
    a = int(input('sua resposta é: '))
    if a == x*y:
     print('resposta correta!')
    else:
     print('A RESPOSTA CORRETA É {}'.format(x*y))
    play = int(input('escreva 1 para jogar novamente ou 0 para sair.'))
else:
    print('obrigado por jogar')

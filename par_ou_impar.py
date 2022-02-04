from time import sleep
from random import randint
play = 'S'
vitorias = 0
while play == 'S':
    esc_pc = randint(1, 11)
    print('Vamos jogar par ou impar!')
    print('SELECIONE SE VOCÊ QUER SER PAR OU IMPAR \n [ P ]PAR [ I ]IMPAR')
    opcao = str(input('digite sua escolha: ').strip().upper())
    if opcao == 'P':
        print('Então eu escolho IMPAR')
        jog = int(input('VAMOS JOGAR! ESCOLHA UM NÚMERO DE 1 A 10: '))
        print('par')
        sleep(1)
        print('ou')
        sleep(1)
        print('impar')
        sleep(1)
        print('-'*10)
        print(f'você jogou {jog} \n eu joguei {esc_pc}')
        print('-'*10)
        soma = jog + esc_pc
        if soma % 2 == 0:
            print('O JOGADOR VENCEU!!')
            vitorias += 1
        else:
            print('O JOGADOR PERDEU!!')
        play = str(input('gostaria de jogar novamente? [ S/N ]: ').strip().upper())
        print('obrigado por jogar')
        print(f'o seu total de vitórias foi {vitorias}')
    if opcao == 'I':
        print('Então eu escolho PAR')
        jog = int(input('VAMOS JOGAR! ESCOLHA UM NÚMERO DE 1 A 10: '))
        print('par')
        sleep(1)
        print('ou')
        sleep(1)
        print('impar')
        sleep(1)
        print('-' * 10)
        print(f'você jogou {jog} \n eu joguei {esc_pc}')
        print('-' * 10)
        soma = jog + esc_pc
        if soma % 2 == 0:
            print('O JOGADOR PERDEU!!')
        else:
            print('O JOGADOR VENCEU!!')
            vitorias += 1
        play = str(input('gostaria de jogar novamente? [S/N]: ').strip().upper())
        print('obrigado por jogar')
        print(f'o seu total de vitórias foi {vitorias}')
nome_jogador_0 = input()
pontuacao_jogador_0 = int(input())
nome_jogador_1 = input()
pontuacao_jogador_1 = int(input())
nome_jogador_2 = input()
pontuacao_jogador_2 = int(input())
nome_jogador_campeao = 'Lucas Lima'

if nome_jogador_0 == nome_jogador_campeao:
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
elif nome_jogador_1 == nome_jogador_campeao:
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
elif nome_jogador_2 == nome_jogador_campeao:
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!')
else:
    if pontuacao_jogador_0 > pontuacao_jogador_1 and pontuacao_jogador_0 > pontuacao_jogador_2:
        print(f'{nome_jogador_0} é eleito o bola de ouro!')
    elif pontuacao_jogador_1 > pontuacao_jogador_0 and pontuacao_jogador_1 > pontuacao_jogador_2:
        print(f'{nome_jogador_1} é eleito o bola de ouro!')
    else:
        print(f'{nome_jogador_2} é eleito o bola de ouro!')
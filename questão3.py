#Inputs:
nome_jogador1 = input()
pontuacao_jogador1 = int(input())
nome_jogador2 = input()
pontuacao_jogador2 = int(input())
nome_jogador3 = input()
pontuacao_jogador3 = int(input())

#Jogadores destaques:
jogador_europeu = 'Rodri'
jogador_brasileiro = 'Vini Jr.'

#Outputs:
if (nome_jogador1 == jogador_europeu):
    print(f'O melhor jogador do mundo é {jogador_europeu}, com {pontuacao_jogador1} ponto(s).')
    print('Os europeus, como sempre, roubaram o nosso ouro!')
elif (nome_jogador2 == jogador_europeu):
    print(f'O melhor jogador do mundo é {jogador_europeu}, com {pontuacao_jogador2} ponto(s).')
    print('Os europeus, como sempre, roubaram o nosso ouro!')
elif (nome_jogador3 == jogador_europeu):
    print(f'O melhor jogador do mundo é {jogador_europeu}, com {pontuacao_jogador3} ponto(s).')
    print('Os europeus, como sempre, roubaram o nosso ouro!')
else:
    if ((pontuacao_jogador1 >= pontuacao_jogador2) and (pontuacao_jogador1 >= pontuacao_jogador3)):
        if nome_jogador1 == jogador_brasileiro:
            print(f'O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s).')
            print('Os brasileiros amaram o resultado! BAILA VINI!')
        else:
            print(f'O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s).')
            print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')
        melhor_jogador = nome_jogador1
        pontuacao_jogador = pontuacao_jogador1
    elif((pontuacao_jogador2 >= pontuacao_jogador1) and (pontuacao_jogador2 >= pontuacao_jogador3)):
        if nome_jogador2 == jogador_brasileiro:
            print(f'O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s).')
            print('Os brasileiros amaram o resultado! BAILA VINI!')
        else:
            print(f'O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s).')
            print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')
        melhor_jogador = nome_jogador2
        pontuacao_jogador = pontuacao_jogador2
    elif ((pontuacao_jogador3 >= pontuacao_jogador1) and (pontuacao_jogador3 >= pontuacao_jogador2)):
        if nome_jogador3 == jogador_brasileiro:
            print(f'O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s).')
            print('Os brasileiros amaram o resultado! BAILA VINI!')
        else:
            print(f'O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s).')
            print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')
        melhor_jogador = nome_jogador3
        pontuacao_jogador = pontuacao_jogador3
#Inputs:
plateia1 = input()
plateia2 = input()
jogador_vencedor= input()

#Nome dos amigos de Palé:
amigo1 = 'Gavião Bonito'
amigo2 = 'Ronaldinho Paulista'

#Nome dos possíveis vendecores:
nome1 = 'Mãodona'
nome2 = 'Palé'

#Outputs:
if ((amigo1 == plateia1 or amigo1 == plateia2) and (amigo2 == plateia1 or amigo2 == plateia2) or jogador_vencedor == nome2):
        print('Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!')
elif ((amigo1 != plateia1 and amigo1 != plateia2) and (amigo2 != plateia1 and amigo2 != plateia2) and jogador_vencedor == nome1):
        print('PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.')
elif ((amigo1 == plateia1 or amigo1 == plateia2) and (amigo2 != plateia1 or amigo2 != plateia2) and jogador_vencedor == nome1):
        print('Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…')
elif ((amigo1 != plateia1 or amigo1 != plateia2) and (amigo2 == plateia1 or amigo2 == plateia2) and jogador_vencedor == nome1):
        print('Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…')
elif ((amigo1 != plateia1 or amigo1 != plateia2) and (amigo2 != plateia1 or amigo2 != plateia2) and (nome1 != jogador_vencedor or nome2 != jogador_vencedor)):
        print('Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.')
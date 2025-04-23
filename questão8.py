# Inputs:
nome_jogador = input()
qtd_partidas = int(input())
qtd_gols = int(input())
qtd_assistencias = int(input())
qtd_desarmes = int(input())
liga_atuante = input()

# Ligas elegiveis (ou consideradas) para a Premiação:
liga_considerada1 = 'Premier League'
liga_considerada2 = 'La Liga'
liga_considerada3 = 'Serie A'
liga_considerada4 = 'Brasileirão'

# Médias da quantidade de gols, assistências e desarmes por partida:
media_gols = qtd_gols / qtd_partidas
media_assistencias = qtd_assistencias / qtd_partidas
media_desarmes = qtd_desarmes / qtd_partidas

# Calculo do score do jogador:
score_jogador = ((qtd_gols * 2) + (qtd_assistencias * 1) + (qtd_desarmes * 0.4))

# Condicional para calcular o score total com base na liga do jogador:
if(liga_atuante == liga_considerada1):
    score_jogador = score_jogador * 1
elif(liga_atuante == liga_considerada2):
    score_jogador= score_jogador * 0.95
elif(liga_atuante == liga_considerada3):
    score_jogador = score_jogador * 0.9
elif(liga_atuante == liga_considerada4):
    score_jogador = score_jogador * 0.8

# Output:
if(liga_atuante == liga_considerada1 or liga_atuante == liga_considerada2 or liga_atuante == liga_considerada3 or liga_atuante == liga_considerada4):
    if(media_gols >= 0.3):
        if(media_assistencias >= 0.15):
            if(media_desarmes >= 1.25):
                if(qtd_partidas >= 50):
                    if(score_jogador >= 80):
                        print(f'Promissor! {nome_jogador} é um potencial ganhador da Bola de Ouro!')
                    elif(score_jogador >= 70 and score_jogador < 80):
                        print(f'{nome_jogador} tem chances médias de ganhar o prêmio.')
                    else:
                        print(f'{nome_jogador} dificilmente ganhará a premiação, apesar de ser apto.')
                else:
                    print('O atleta não jogou partidas o suficiente para concorrer à premiação.')
            else:
                print(f'{nome_jogador} não desarmou jogadores o suficiente, portanto está fora.')
        else:
            print('Infelizmente não teve assistências o suficiente, portanto não concorre ao prêmio.')
    else:
        print('O jogador está fora, não possui a média de gols necessária.')
else:
    print('A liga informada não é válida ou o jogador não pertence a nenhuma das ligas elegíveis para a premiação.')

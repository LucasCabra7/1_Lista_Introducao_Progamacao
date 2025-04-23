# Inputs:
nome_jogador_votado1= input()
origem_jurado1 = input()
nome_jogador_votado2= input()
origem_jurado2 = input()

# Variaveis para os países de cada jogador:
pais_vinicius = 'Brasil'
pais_rodri = 'Espanha'

# Variaveis para o nomes dos jogadores:
jogador_vini = 'vinijr'
jogador_rodri = 'rodri'

# Variaveis para quantidade inicial de votos de cada jogador:
qtd_votos_vinicius = 0
qtd_votos_rodri = 0

# Outputs:
if (nome_jogador_votado1 == jogador_vini):
    if(origem_jurado1 == pais_vinicius):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')
elif(nome_jogador_votado1 == jogador_rodri):
    if(origem_jurado1 == pais_rodri):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')
if (nome_jogador_votado2 == jogador_vini):
    if(origem_jurado2 == pais_vinicius):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')
elif(nome_jogador_votado2 == jogador_rodri):
    if(origem_jurado2 == pais_rodri):
        print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')
    else:
        print('Voto registrado!')

if(nome_jogador_votado1 == jogador_vini):
    if(origem_jurado1 == pais_vinicius):
        qtd_votos_vinicius += 0
    else:
        qtd_votos_vinicius += 1
elif(nome_jogador_votado1 == jogador_rodri):
    if(origem_jurado1 == pais_rodri):
        qtd_votos_rodri += 0
    else:
        qtd_votos_rodri += 1

if(nome_jogador_votado2 == jogador_vini):
    if(origem_jurado2 == pais_vinicius):
        qtd_votos_vinicius += 0
    else:
        qtd_votos_vinicius += 1
elif(nome_jogador_votado2 == jogador_rodri):
    if(origem_jurado2 == pais_rodri):
        qtd_votos_rodri += 0
    else:
        qtd_votos_rodri += 1

print(f'Votos válidos para {jogador_rodri}: {qtd_votos_rodri}')
print(f'Votos válidos para {jogador_vini}: {qtd_votos_vinicius}')
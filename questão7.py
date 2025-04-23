# Inputs:
nome_jogador1 = input()
qtd_gols_jogador1 = int(input())
qtd_partidas_jogador1 = int(input())
speed_max_jogador1 = float(input())
nome_jogador2 = input()
qtd_gols_jogador2 = int(input())
qtd_partidas_jogador2 = int(input())
speed_max_jogador2 = float(input())
nome_jogador3 = input()
qtd_gols_jogador3 = int(input())
qtd_partidas_jogador3 = int(input())
speed_max_jogador3 = float(input())

# Tamanho do nome de cada jogador:
tamanho_nome_jogador1 = len(nome_jogador1)
tamanho_nome_jogador2 = len(nome_jogador2)
tamanho_nome_jogador3 = len(nome_jogador3)

# Resultado final com a média ponderada para cada jogador:
resultado_final_jogador1 = ((((qtd_gols_jogador1 * 5) + (qtd_partidas_jogador1 * 2) + (speed_max_jogador1 * 3)) / 10) + (tamanho_nome_jogador1 % 3))
resultado_final_jogador2 = ((((qtd_gols_jogador2 * 5) + (qtd_partidas_jogador2 * 2) + (speed_max_jogador2 * 3)) / 10) + (tamanho_nome_jogador2 % 3))
resultado_final_jogador3 = ((((qtd_gols_jogador3 * 5) + (qtd_partidas_jogador3 * 2) + (speed_max_jogador3 * 3)) / 10) + (tamanho_nome_jogador3 % 3))

# Output:
if((resultado_final_jogador1 >= resultado_final_jogador2) and (resultado_final_jogador1 >= resultado_final_jogador3)):
    primeiro_lugar = nome_jogador1
    resultado_ganhador1 = resultado_final_jogador1
    if(resultado_final_jogador2 >= resultado_final_jogador3):
        segundo_lugar = nome_jogador2
        terceiro_lugar = nome_jogador3
        resultado_ganhador2 = resultado_final_jogador2
        resultado_ganhador3 = resultado_final_jogador3
    else:
        segundo_lugar = nome_jogador3
        terceiro_lugar = nome_jogador2
        resultado_ganhador2 = resultado_final_jogador3
        resultado_ganhador3 = resultado_final_jogador2
elif((resultado_final_jogador2 >= resultado_final_jogador1) and (resultado_final_jogador2 >= resultado_final_jogador3)):
    primeiro_lugar = nome_jogador2
    resultado_ganhador1 = resultado_final_jogador2
    if(resultado_final_jogador1 >= resultado_final_jogador3):
        segundo_lugar = nome_jogador1
        terceiro_lugar = nome_jogador3
        resultado_ganhador2 = resultado_final_jogador1
        resultado_ganhador3 = resultado_final_jogador3
    else:
        segundo_lugar = nome_jogador3
        terceiro_lugar = nome_jogador1
        resultado_ganhador2 = resultado_final_jogador3
        resultado_ganhador3 = resultado_final_jogador1
elif((resultado_final_jogador3 >= resultado_final_jogador1) and (resultado_final_jogador3 >= resultado_final_jogador2)):
    primeiro_lugar = nome_jogador3
    resultado_ganhador1 = resultado_final_jogador3
    if(resultado_final_jogador1 >= resultado_final_jogador2):
        segundo_lugar = nome_jogador1
        terceiro_lugar = nome_jogador2
        resultado_ganhador2 = resultado_final_jogador1
        resultado_ganhador3 = resultado_final_jogador2
    else:
        segundo_lugar = nome_jogador2
        terceiro_lugar = nome_jogador1
        resultado_ganhador2 = resultado_final_jogador2
        resultado_ganhador3 = resultado_final_jogador1


print(f'1 - {primeiro_lugar} obteve {resultado_ganhador1:.2f} pontos.')
print(f'2 - {segundo_lugar} obteve {resultado_ganhador2:.2f} pontos.')
print(f'3 - {terceiro_lugar} obteve {resultado_ganhador3:.2f} pontos.')
print(f'{primeiro_lugar} é o verdadeiro ganhador da Bola de Ouro com um total de {resultado_ganhador1:.2f} pontos.')


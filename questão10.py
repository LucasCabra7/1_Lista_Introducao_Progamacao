# Inputs:
projecao_desempenho = input()
projecao_participacao_gols = int(input())
desempenho_final = input()

# Print inicial da execução do programa:
print('Está aberta a revisão da premiação!')

# Variáveis com a pontuação total, iniciando com zero, do Vinijr e a participação de Gols:
pontuacao_total_vini = 0
participacao_gols_vini = 37

# Variáveis com a ponutação total do rodri e o seu desempenho na temporada:
pontuacao_total_rodri = 1170
desempenho_final_rodri = 'Importante'

# Análise da Projeção de Desempenho para a temporada:
if(projecao_desempenho == 'Decepção'):
    pontuacao_total_vini = pontuacao_total_vini + 100
    print('Parece que não estão colocando muitas expectativas para a temporada do nosso Vini Jr., não... Sempre subestimado!')
elif(projecao_desempenho == 'Oscilação'):
    pontuacao_total_vini = pontuacao_total_vini + 200
    print('Os jornalistas acreditam que Vini Jr. terá atuações irregulares nesta temporada, mas quem sabe ele não supera as projeções?')
elif(projecao_desempenho == 'Importante'):
    pontuacao_total_vini = pontuacao_total_vini + 300
    print('Em um elenco tão forte como o do Real Madrid, é normal as atenções serem divididas mesmo. O que importa é que ele não vai se esconder!')
elif(projecao_desempenho == 'Estrela'):
    pontuacao_total_vini = pontuacao_total_vini + 400
    print('Vini Jr. será o craque do Real Madrid na temporada de 2023/2024! Será que ele consegue a tão sonhada Bola de Ouro?')

# Análise da Projeção de Participação em Gols para a temporada e adicionando o resultado final a pontuação total do vini:
pontuacao_da_projecao_gols = ((2 * projecao_participacao_gols) + (pontuacao_total_vini / 2))
pontuacao_total_vini = pontuacao_total_vini + pontuacao_da_projecao_gols

#Análise do Desempenho Final de Vini Jr. ao fim da temporada:
if(desempenho_final == 'Decepção'):
    pontuacao_total_vini = pontuacao_total_vini + 150
    print('Vini Jr. decepcionou os torcedores em 2024, não era o ano dele.')
elif(desempenho_final == 'Oscilação'):
    pontuacao_total_vini = pontuacao_total_vini + 250
    print('A temporada não foi das melhores, mas Vini Jr. conseguiu mostrar, em alguns momentos, que ele de fato é craque.')
elif(desempenho_final == 'Importante'):
    pontuacao_total_vini = pontuacao_total_vini + 350
    print('Vini Jr. mostrou que é crucial para o elenco do Real Madrid e da Seleção.')
elif(desempenho_final == 'Estrela'):
    pontuacao_total_vini = pontuacao_total_vini + 500
    print('Ele é demais! Herói do título da Champions, ele conseguiu mostrar ao mundo que é uma estrela do futebol!')

# Comparação entre a Projeção de Desempenho e o Desempenho Final ao fim da temporada:
if((desempenho_final == 'Estrela') and (projecao_desempenho == 'Importante' or projecao_desempenho == 'Oscilação' or projecao_desempenho == 'Decepção')):
    pontuacao_total_vini = pontuacao_total_vini + 300
    print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
elif((desempenho_final == 'Importante') and (projecao_desempenho == 'Oscilação' or projecao_desempenho == 'Decepção')):
    pontuacao_total_vini = pontuacao_total_vini + 300
    print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
elif((desempenho_final == 'Oscilação') and (projecao_desempenho == 'Decepção')):
    pontuacao_total_vini = pontuacao_total_vini + 300
    print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
elif((projecao_desempenho == 'Estrela') and (desempenho_final == 'Importante' or desempenho_final == 'Oscilação' or desempenho_final == 'Decepção')):
    print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif((projecao_desempenho == 'Importante') and (desempenho_final == 'Oscilação' or desempenho_final == 'Decepção')):
    print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif((projecao_desempenho == 'Oscilação') and (desempenho_final == 'Decepção')):
    print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')
elif(projecao_desempenho == desempenho_final):
    pontuacao_total_vini = pontuacao_total_vini + 100
    print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')

# Comparação entre a participação de Gols do vini na temporada e a projeção de participação de gols:
if(participacao_gols_vini >= projecao_participacao_gols):
    print('Vini Jr. foi muito decisivo para sua equipe este ano, superando sua previsão de participações em gols!')
else:
    print('É, Vini Jr. não conseguiu provar que estavam errados, mas ainda assim ele segue vivo para a premiação.')

# Determinação do Resultado Final entre vini e rodri, e também o critério de desempate:
if(pontuacao_total_vini > pontuacao_total_rodri):
    print(f'O mundo estava certo! Com {pontuacao_total_vini:.0f} pontos, Vini Malvadeza é o verdadeiro melhor do mundo! Chega dessa injustiça!')
elif(pontuacao_total_vini < pontuacao_total_rodri):
    print('Infelizmente, teremos que nos contentar com o Rodri sendo o melhor do mundo mesmo.')
else:
    print('Empate! Vamos ao critério de desempate.')
    if (pontuacao_total_vini == pontuacao_total_rodri):
        if (desempenho_final == 'Estrela'):
            print('Foi uma premiação apertada, mas a justiça foi feita! Vini Jr. é, sim, o melhor do mundo.')
        elif (desempenho_final == 'Importante' or desempenho_final == 'Oscilação' or desempenho_final == 'Decepção'):
            print('Bom, é isso. Ainda tivemos esperanças, mas o Rodri é, mesmo, o Bola de Ouro.')
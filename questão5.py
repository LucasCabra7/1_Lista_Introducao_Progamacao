# Inputs:
orcamento_total = float(input())
numero_convidados = int(input())
local_festa = input()
cantor_convidado = input()
valor_euro = float(input())

# Valor da conversão de Reais para Euros:
valor_convertido = orcamento_total / valor_euro

# Valor da quantidade de gastos por convidados:
gasto_por_convidado = valor_convertido / numero_convidados

# Nomes dos possíveis locais para festa:
hotel1 = 'Hotel Pera Palace'
hotel2 = 'Hotel Copacabana Palace'

# Nome dos possiveis cantores convidados:
cantor1 = 'Anitta'
cantor2 = 'Thiaguinho'

# Outputs:
if (valor_convertido < 1000000):
    print(f'Acabei de receber a informação que o orçamento total da festa será {valor_convertido:.2f} de euros. Poxa, com um orçamento desses vai ser difícil fazer a festa bombar! Vou divulgar essa informação pros sites de fofocas pra flopar a festa.')
else:
    print('Poxa, esse cara tá podendo! Vai ser um festão, mas eu vou encontrar alguma coisa para que flope.')

if (gasto_por_convidado >= 5000):
    print('Eita, cancela o repasse da informação pros sites de fofocas! Gastando isso tudo por pessoa, vai continuar sendo um luxo.')
else:
    print('Que vergonha, viu? O povo vai passar fome. Divulgue isso agora!')

if(local_festa == hotel1 or local_festa == hotel2):
    print('Eu conheço os donos e são meus amigos! Vou pedir pra recusarem a oferta!')
else:
    print('Poxa, não vou conseguir fazer nada!')

if(cantor_convidado == cantor1 or cantor_convidado == cantor2):
    print(f'Duvido que aceite, Rodri fez isso pra me estressar! Claro que {cantor_convidado} não vai fazer isso comigo!')
else:
    print('Vou fazer uma oferta maior! Isso precisa flopar!')

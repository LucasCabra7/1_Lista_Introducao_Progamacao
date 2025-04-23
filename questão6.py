# Inputs:
taxa_f1 = float(input())
taxa_v1 = float(input())
taxa_f2 = float(input())
taxa_v2 = float(input())

# Variáveis para as empresas:
e1 = 'Empresa 1'
e2 = 'Empresa 2'

# Outputs:
# Condicional para as funções que independem da variável K:
if((taxa_v1 < taxa_v2) and (taxa_f2 > taxa_f1)):
    print(f'A {e1} é sempre a melhor opção!')
elif((taxa_v1 == taxa_v2) and (taxa_f2 > taxa_f1)):
    print(f'A {e1} é sempre a melhor opção!')
elif((taxa_v2 < taxa_v1) and (taxa_f1 > taxa_f2)):
    print(f'A {e2} é sempre a melhor opção!')
elif((taxa_v2 == taxa_v1) and (taxa_f1 > taxa_f2)):
    print(f'A {e2} é sempre a melhor opção!')
elif((taxa_v1 == taxa_v2) and (taxa_f2 == taxa_f1)):
    print('As duas empresas possuem o mesmo preço sempre!')
else:
    # Formúla para o valor da função que depende da variável K:
    k = (taxa_f2 - taxa_f1) / (taxa_v1 - taxa_v2)
    
    # Condicional para função que depende da variável K:
    if(k >= 0):
        if(taxa_v1 < taxa_v2):
            print(f'{e2} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {e1} é mais barata para distâncias maiores que {k:.2f} km.')
        elif(taxa_v1 > taxa_v2):
            print(f'{e1} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {e2} é mais barata para distâncias maiores que {k:.2f} km.')
    else:
        if(taxa_v1 < taxa_v2):
            print(f'{e1} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {e2} é mais barata para distâncias maiores que {k:.2f} km.')

        elif(taxa_v1 > taxa_v2):
            print(f'{e2} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {e1} é mais barata para distâncias maiores que {k:.2f} km.')
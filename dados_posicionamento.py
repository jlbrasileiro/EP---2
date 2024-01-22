#dicionario para tamanho dos navios
dados_navio = {'Submarinos': 1, 'Contratorpedeiro': 2, 'Navio-Tanque': 3, 'Porta-aviões': 4}


#Dados do dicionário
dados = {}

i = True
while i:

    #Posição X
    print('\nEscolha um número de 0 a 10 para seu X.')
    linha = int(input('Escolha um X: '))
    if linha > 10:
        print('Digite um número de 0 a 10.')
    dados['linha'] = linha

    #Posição Y
    print('\nEscolha um número de 0 a 10 para seu Y.')
    coluna = int(input('Escolha um Y: '))
    if coluna > 10:
        print('Digite um número de 0 a 10')
    dados['coluna'] = coluna
    
    #tamanho dos navios
    print('\nDigite dentre os tamanhos dispóniveis')
    tamanho_navio = int(input('Qual tamanho do seu navio? '))
    dados['tamanho'] = tamanho_navio
        
    #Orientação do navio
    print('\nSua orientação pode ser na vertical ou na horizontal')
    orientacao = str(input('Qual sua orientação? '))
    if orientacao != 'vertical' or 'horizontal':
        print('Digite vertical ou horizontal')
    dados['orientacao'] = orientacao
    i = False

    print(f'\n{dados}')




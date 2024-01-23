#dicionario para tamanho dos navios
dados_navio = {'Submarinos': 1, 'Contratorpedeiro': 2, 'Navio-Tanque': 3, 'Porta-aviões': 4}

#strings com nomes dos navios
nome_navio = ['Submarinos','Contratorpedeiro','Navio-Tanque','Porta-aviões']

#Dados do dicionário
#def dados_dicionario():
dados = {}

i = True
while i:

    #Posição X
    print('\nEscolha um número de 0 a 10 para seu X.')
    linha = int(input('Escolha um X: '))
    if linha > 10:
        print('Por favor, digite um número de 0 a 10.')

    dados['linha'] = linha

    #Posição Y
    print('\nEscolha um número de 0 a 10 para seu Y.')
    coluna = int(input('Escolha um Y: '))
    if coluna > 10:
        print('Por favor, digite um número de 0 a 10.')

    dados['coluna'] = coluna
    
    #Tamanho dos navios
    print('\nDigite dentre os tamanhos dispóniveis')
    tamanho_navio = int(input('Qual tamanho do seu navio? '))

    dados['tamanho'] = tamanho_navio
        
    #Orientação do navio
    print('\nSua orientação pode ser na vertical ou na horizontal')
    orientacao = input('Qual sua orientação? ')
    #if orientacao != 'vertical' or orientacao != 'horizontal':
        #print('Por favor, digite "vertical" ou "horizontal".')

    dados['orientacao'] = orientacao
    break

print(dados)


#lista de posicoes
#posicoes = []
#cont = 0
#while True:
 #   if orientacao == 'horizontal':
  #      posicoes[0] = linha
   #     posicoes.append(posicoes[0])
    #    posicoes[1] = coluna + cont
     #   posicoes.append(posicoes[1])
      #  cont += 1






#print(f'\n{dados}')

#Dados do posicionamento dos tiros, frota.
#frota = [{'tipo': 'navio-tanque', 'posicoes': [[6, 1], [6, 2], [6, 3]]}]
#dados_frota = {}
#lista_posicoes = [[]]
#frota = []

#dados_frota = {}
#for nome in nome_navio:
 #   dados_frota['tipo'] = nome

#print(dados_frota)




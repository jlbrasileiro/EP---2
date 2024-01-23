linha = int(input('X: '))
coluna = int(input('Y: '))
orientacao = input('Qual orientacao: ')
tamanho = int(input('Tamanho do navio: '))

posicoes = []
cont = 0

while True:
    if orientacao == 'horizontal':
        posicoes[0] = linha
        posicoes[1] = (coluna + cont) 

    elif orientacao == 'vertical':
        posicoes[0] = (linha + cont)
        posicoes[1] = coluna

    cont +=1
    
    print(posicoes) 
        
        #posicoes.append(linha[0])

        #posicoes[0] = linha
        #posicoes.append(posicoes[0])
        #posicoes[1] = coluna + cont
        #posicoes.append(posicoes[1])
        #cont += 1
    #print(posicoes)
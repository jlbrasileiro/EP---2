def define_posicoes(posicionamento):
    #definindo linha, coluna, orientaçao e tamanho
    linha = posicionamento['linha']
    coluna = posicionamento['coluna']
    orientacao = posicionamento['orientacao']
    tamanho = posicionamento['tamanho']
    #criando lista vazia das posições 
    posicoes = []
    #adcionando as sublistas com as posições
    if orientacao == 'vertical':
        for i in range(linha, linha + tamanho):
            posicoes.append([i, coluna])
    elif orientacao == 'horizontal':
        for j in range(coluna, coluna + tamanho):
            posicoes.append([linha, j])

    return posicoes

def define_posicoes(dados_de_posicionamento):
    #definindo linha, coluna, orientaçao e tamanho
    linha = dados_de_posicionamento['linha']
    coluna = dados_de_posicionamento['coluna']
    orientacao = dados_de_posicionamento['orientacao']
    tamanho = dados_de_posicionamento['tamanho']
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
def preenche_frota(dados_de_posicionamento, nome_navio, frota):
    posicoes = define_posicoes(dados_de_posicionamento)

    navio = {
        'tipo': nome_navio,
        'posicoes': posicoes
    }

    frota.append(navio)

    return frota 
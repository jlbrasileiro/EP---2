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
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for navio in frota:
        for coordenada in navio['posicoes']:
            tabuleiro[coordenada[0]][coordenada[1]] = 1

    return tabuleiro
def afundados(frota,tabuleiro):
    navios_afundados = 0
    for navio in frota:
        todos_uns_afundados = True
        for coordenada in navio['posicoes']:
            if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                todos_uns_afundados = False
                break
        if todos_uns_afundados:
                navios_afundados += 1
    return navios_afundados

def posicao_valida(dados_de_posicionamento,frota):
    novas_posicoes = define_posicoes(dados_de_posicionamento)
    for navio in frota:
        for posicao in novas_posicoes:
            if posicao in navio['posicoes']:
                return False
    for posicao in novas_posicoes:
        if posicao[0] < 0 or posicao[0] >= 10 or posicao[1] < 0 or posicao[1] >= 10:
            return False
    return True


    
def define_posicoes(dados_de_posicionamento):
    linha = dados_de_posicionamento["linha"]
    coluna = dados_de_posicionamento["coluna"]
    orientacao = dados_de_posicionamento["orientacao"]
    tamanho = dados_de_posicionamento["tamanho"]

    posicoes = []

    if orientacao == "vertical":
        for i in range(linha, linha + tamanho):
            posicoes.append([i, coluna])
    elif orientacao == "horizontal":
        for j in range(coluna, coluna + tamanho):
            posicoes.append([linha, j])

    return posicoes

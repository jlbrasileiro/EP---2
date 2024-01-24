print(f'\n{"*"*10} Bem vindas(os) ao jogo \033[1;31;43m Batalha Naval \033[m !!! {"*"*10}\n')
print('\n• Seu objetivo será tentar afundar todos os navios inimigos.\n• Seus navios são posicionados de forma automática no começo do jogo, conte com a sorte! :)\n')
print(f'\n\033[1;31;43m Navios disponivéis:\033[m\n➞ 4 Submarinos de tamanho 1.\n➞ 3 Contratorpedeiro de tamanho 2.\n➞ 2 Navio-Tanque de tamanho 3.\n➞ 1 Porta-aviões de tamanho 4.\n\n')

import random
from funcoes import *

# PARA TESTAR O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
coordenadas_ja_informadas = []
coordenadas_ja_informadas_oponentes =[]
while jogando:

    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    validacao_repetida = True
    while validacao_repetida:
        
        linha = int(input('Qual linha deseja atacar?: '))
        while linha > 9 or linha < 0:
            print('Linha inválida!')
            linha = int(input('Qual linha deseja atacar?: '))

        
        coluna = int(input('Qual coluna deseja atacar: '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Qual coluna deseja atacar: '))

   
        if [linha, coluna] in coordenadas_ja_informadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            validacao_repetida = False
            coordenadas_ja_informadas.append([linha, coluna])

    resultado_jogada = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False  

    
      
    if afundados(frota_oponente,tabuleiro_oponente) < len(frota_oponente):
        linha_oponente = random.randint(0,9)
        coluna_oponente = random.randint(0,9)

        while [linha_oponente,coluna_oponente] in coordenadas_ja_informadas_oponentes:
            linha_oponente = random.randint(0,9)
            coluna_oponente = random.randint(0,9)
        coordenadas_ja_informadas_oponentes.append([linha_oponente,coluna_oponente])

        jogada_oponente = faz_jogada(tabuleiro_jogador,linha_oponente,coluna_oponente)
        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')


        if afundados(frota_jogador,tabuleiro_jogador) == len(frota_jogador):
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
    else:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando =  False

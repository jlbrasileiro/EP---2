#Parte de ver a linha e coluna e se tiver na lista diz que ja tem

jogando = True
lista = []
while jogando:    
                   
            # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
            validacao_repetida = True
            while validacao_repetida:

                print('\nEscolha um número de 0 a 9 para sua linha.')
                linha = int(input('Qual linha deseja atacar: '))

                while linha > 9 or linha < 0:
                    print('Linha inválida!')
                    #pergunta de novo
                    linha = int(input('Qual linha deseja atacar: '))
                    #if linha in lista:
                     #       print('oi')

        
                # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
                print('\nEscolha um número de 0 a 9 para sua coluna.')
                coluna = int(input('Qual coluna deseja atacar: '))

                while coluna < 0 or coluna > 9:
                    print('Coluna inválida!')
                    #pergunta de novo
                    coluna = int(input('Qual coluna deseja atacar: '))
                    
                if [linha,coluna] in lista:
                    print('já existe')
                    validacao_repetida = False
                
                else:
                    validacao_repetida = True  
                    lista.append([linha,coluna])


print('láisa é linda')

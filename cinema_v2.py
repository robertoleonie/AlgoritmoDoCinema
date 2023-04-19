import random
import math

# cria uma sala de cinema inicialmente vazia
# o cinema sera uma bit matrix:
# 0 := assento cinema[i][j] vazio
# 1 := assento cinema[i][j] ocupado
def createCinema(lin, col) :
    cinema = [[0]*col for row in range(lin)]
    return cinema

# funcao que acomoda o individuo na poltrona de fileira e coluna escolhidos
# @param
# cinema := a sala de cinema passada como entrada
# people := qual o individuo (iteravel) que esta escolhendo aquela poltrona
# intendedRow := a fileira escolhida pelo individuo
# intendedColumn := a coluna escolhida pelo individuo
# seated := um flag de controle determinando se o individuo ja sentou
def sitAtTheSeat(cinema, people, intendedSeat, seated=True) :
    # calculo da fileira e coluna para sentar
    intendedRow = math.floor(intendedSeat/len(cinema[0]))
    intendedColumn = intendedSeat % len(cinema[0])
    
    cinema[intendedRow][intendedColumn] = 1    
    seated = True   # confirmo o individuo como ja acomodado

    # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
    print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
          % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
    latestRow = intendedRow
    latestColumn = intendedColumn

    return cinema, latestRow, latestColumn

# 1. ALGORITMO CLASSICO DE POPULAR UMA SALA DE CINEMA
# k pessoas compram seus ingressos para assistir a um filme
# o cinema gerado eh inicialmente vazio
def populateClassicAlgorithm(k, cinema) :
    # lin := o numero de fileiras da sala de cinema
    # col := o numero de colunas da sala de cinema
    lin = len(cinema)
    col = len(cinema[0])

    # futuramente, vamos desejar retornar a fileira e a coluna
    # do ultimo individuo que entrou na sala de cinema
    # como parte de uma tupla

    # "lazy initialization"
    latestRow = 0
    latestColumn = 0

    # se o numero de individuos comprando ingressos for maior do que
    # o tamanho da sala de cinema, so coloco para dentro os lin*col primeiros
    if(k > lin*col) :
        return populateClassicAlgorithm(lin*col, cinema)

    for people in range(k) :
        # variavel de controle booleana que diz se o individuo ja sentou
        seated = False

        while (not seated) :
            # o individuo escolhe uma poltrona no intervalo [0, lin*col) para sentar
            intendedSeat = random.randrange(0, lin*col)

            # calculo da fileira e coluna para sentar
            intendedRow = math.floor(intendedSeat/col)
            intendedColumn = intendedSeat % col

            # testando se o assento escolhido esta vazio
            if (cinema[intendedRow][intendedColumn] == 0) :
                # PRIORIDADE MAIS ALTA: O INDIVIDUO EVITARA SENTAR IMEDIATAMENTE ATRAS
                # DE UMA POLTRONA QUE JA ESTEJA OCUPADA

                # primeiro precisamos testar se o individuo escolheu sentar na primeira fileira.
                # caso positivo, nao eh necessario testar a frente. somente para a vizinhança dos lados
                if (intendedRow == 0) :
                    # testa se a poltrona escolhida esta na fileira mais a direita do cinema
                    if (intendedColumn == 0) :
                        # testa se a poltrona imediatamente a esquerda da escolhida esta VAZIA
                        if (cinema[intendedRow][intendedColumn+1] == 0) :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                  % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # se a poltrona imediatamente a esquerda da escolhida esta ocupada
                        else :
                            # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                            if (people < (lin*col) - 1) :
                                # realiza uma nova busca por poltronas
                                continue

                            # se a sala de cinema realmente esta cheia exceto pela poltrona escolhida,
                            # o individuo obrigatoriamente tera de se sentar naquela poltrona 
                            else :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                    # testa se a poltrona escolhida esta na fileira mais a esquerda do cinema
                    if (intendedColumn == col-1) :
                        # testa se a poltrona imediatamente a direita da escolhida esta VAZIA
                        if (cinema[intendedRow][intendedColumn-1] == 0) :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                  % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # se a poltrona imediatamente a esquerda da escolhida esta ocupada
                        else :
                            # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                            if (people < (lin*col) - 1) :
                                # realiza uma nova busca por poltronas
                                continue

                            # se a sala de cinema realmente esta cheia exceto pela poltrona escolhida,
                            # o individuo obrigatoriamente tera de se sentar naquela poltrona 
                            else :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                    # testa se a poltrona escolhida pelo individuo NAO ESTA nas pontas da sala de cinema
                    else :
                        # inicialmente, testa se tanto a poltrona imediatamente a esquerda quanto
                        # a poltrona imediatamente a direita estao livres.
                        if (cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 0) :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                  % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # caso negativo, testa se existe alguma poltrona com adjacente da esquerda "XOU" da direita
                        # (nunca as duas) livre.
                        elif ((cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 0) or \
                              (cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 1)) :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                  % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # caso negativo, aceita sentar em uma poltrona com ambas adjacentes ocupadas
                        elif ((cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 1)) :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                  % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                # TESTA SE O INDIVIDUO NAO ESCOLHEU SENTAR NA PRIMEIRA FILEIRA.
                else :  # if (intendedRow > 0) :
                    # testa se a poltrona imediatamente a frente esta livre. se estiver,
                    # pode prosseguir com a analise da fronteira da poltrona escolhida.
                    if (cinema[intendedRow-1][intendedColumn] == 0) :
                        # testa se a poltrona escolhida esta na fileira mais a direita do cinema
                        if (intendedColumn == 0) :
                            # testa se a poltrona imediatamente a esquerda da escolhida esta VAZIA
                            if (cinema[intendedRow][intendedColumn+1] == 0) :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                            # se a poltrona imediatamente a esquerda da escolhida esta ocupada
                            else :
                                # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                                if (people < (lin*col) - 1) :
                                    # realiza uma nova busca por poltronas
                                    continue

                                # se a sala de cinema realmente esta cheia exceto pela poltrona escolhida,
                                # o individuo obrigatoriamente tera de se sentar naquela poltrona 
                                else :
                                    '''cinema[intendedRow][intendedColumn] = 1    
                                    seated = True   # confirmo o individuo como ja acomodado

                                    # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                    print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                          % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                    latestRow = intendedRow
                                    latestColumn = intendedColumn'''
                                    sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # testa se a poltrona escolhida esta na fileira mais a esquerda do cinema
                        if (intendedColumn == col-1) :
                            # testa se a poltrona imediatamente a direita da escolhida esta VAZIA
                            if (cinema[intendedRow][intendedColumn-1] == 0) :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                            # se a poltrona imediatamente a esquerda da escolhida esta ocupada
                            else :
                                # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                                if (people < (lin*col) - 1) :
                                    # realiza uma nova busca por poltronas
                                    continue

                                # se a sala de cinema realmente esta cheia exceto pela poltrona escolhida,
                                # o individuo obrigatoriamente tera de se sentar naquela poltrona 
                                else :
                                    '''cinema[intendedRow][intendedColumn] = 1    
                                    seated = True   # confirmo o individuo como ja acomodado

                                    # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                    print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                          % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                    latestRow = intendedRow
                                    latestColumn = intendedColumn'''
                                    sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                        # testa se a poltrona escolhida pelo individuo NAO ESTA nas pontas da sala de cinema
                        else :
                            # inicialmente, testa se tanto a poltrona imediatamente a esquerda quanto
                            # a poltrona imediatamente a direita estao livres.
                            if (cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 0) :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                            # caso negativo, testa se existe alguma poltrona com adjacente da esquerda "XOU" da direita
                            # (nunca as duas) livre.
                            elif ((cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 0) or \
                                  (cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 1)) :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                            # caso negativo, aceita sentar em uma poltrona com ambas adjacentes ocupadas
                            elif ((cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 1)) :
                                '''cinema[intendedRow][intendedColumn] = 1    
                                seated = True   # confirmo o individuo como ja acomodado

                                # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                                print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                      % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                                latestRow = intendedRow
                                latestColumn = intendedColumn'''
                                sitAtTheSeat(cinema, people, intendedSeat, seated=True)

                    # se a poltrona imediatamente a frente esta ocupada, o individuo escolhera outro lugar
                    # dadas as condicoes da capacidade da sala de cinema.
                    else :
                        # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                        if (people < (lin*col) - 1) :
                            # realiza uma nova busca por poltronas
                            continue

                        # se a sala de cinema realmente esta cheia exceto pela poltrona escolhida,
                        # o individuo obrigatoriamente tera de se sentar naquela poltrona
                        else :
                            '''cinema[intendedRow][intendedColumn] = 1    
                            seated = True   # confirmo o individuo como ja acomodado

                            # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                            print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' \
                                % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                            latestRow = intendedRow
                            latestColumn = intendedColumn'''
                            sitAtTheSeat(cinema, people, intendedSeat, seated=True)

            # a poltrona escolhida esta ocupada. precisa procurar por outra poltrona.
            else :
                # testa se a sala de cinema possui mais de uma poltrona sobrando para uma nova escolha
                if (people < (lin*col) - 1) :
                    # realiza uma nova busca por poltronas
                    continue
                else :
                    print('O cinema esta lotado. Tente novamente em uma outra sessao.')

        return cinema, latestRow, latestColumn

# atraves da passagem da configuracao da sala de cinema como parametro,
# obter a fileira e coluna especificas do assento do proximo espectador,
# baseado no algoritmo classico acima de popular uma sala de cinema.
def getNextSeatClassic(cinema) :
    # eh importante lembrar que a matriz que representa a sala de cinema
    # eh uma estrutura global possivel de ser atualizada em qualquer metodo
    # deste programa. portanto, nao precisamos especificar o indice do proximo
    # espectador a adentrar a sala de cinema
    cinema, fileira, coluna = populateClassic(1, cinema)
    print('O proximo individuo pode sentar na poltrona da fileira %d e coluna %d.' % (fileira+1, coluna+1))


    return cinema, fileira, coluna

# esvaziar a sala de cinema passada como parametro
def emptyCinema(cinema) :
    cinema = createCinema(len(cinema), len(cinema[0]))
    return cinema

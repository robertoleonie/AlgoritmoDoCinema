import random
import math

# cria uma sala de cinema inicialmente vazia
def createCinema(lin, col) :
    cinema = [[0]*col for row in range(lin)]
    return cinema

# ALGORITMO CLASSICO DE POPULAR UMA SALA DE CINEMA
# k pessoas compram ingressos para assistir a um filme
# o cinema gerado inicialmente vazio
def populateClassic(k, cinema) :
    # lin := o numero de fileiras da sala
    # col := o numero de colunas da sala
    lin = len(cinema)
    col = len(cinema[0])

    # futuramente, vamos desejar retornar a fileira e a coluna
    # do ultimo individuo que entrou no cinema
    # "lazy inicialization"
    latestRow = 0
    latestColumn = 0

    for people in range(k) :
        # variavel que diz se o individuo ja sentou
        seated = False
        
        while(not seated) :
            # inicialmente, o individuo possui um assento = [0, lin*col) em mente
            intendedSeat = random.randrange(0, lin*col)
            intendedRow = math.floor(intendedSeat/col)
            intendedColumn = intendedSeat % col

            # testando como PRIORIDADE MAIS ALTA: o individuo ira evitar sentar
            # imediatamente atras de alguma poltrona ocupada para que nao lhe atrapalhe
            # a ver o filme.
            
            # testando se o assento esta vazio
            if(cinema[intendedRow][intendedColumn] == 0) :
                # testando se nao existe algum individuo sentado imediatamente a minha frente
                # logico que esse teste so eh possivel se ele NAO ESTA na primeira fileira
                if(intendedRow > 0 and cinema[intendedRow-1][intendedColumn] == 0) :
                    cinema[intendedRow][intendedColumn] = 1
                        

                    seated = True
                    # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                    print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                    latestRow = intendedRow
                    latestColumn = intendedColumn

                else :
                    # se o cinema nao estiver lotado ou nao estiver com apenas um lugar sobrando
                    if(people < (lin*col)-1) :
                        # nova procura por assentos
                        continue
                    

            # testando se o assento escolhido esta na ponta esquerda
            if(intendedColumn == 0) :
                # testando se o assento esta vazio
                if(cinema[intendedRow][intendedColumn] == 0) :
                    # testando se existe gente sentada imediatamente a sua esquerda
                    if(cinema[intendedRow][intendedColumn+1] == 0) :
                        cinema[intendedRow][intendedColumn] = 1
                        
                        seated = True
                        # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                        print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                        latestRow = intendedRow
                        latestColumn = intendedColumn

                    else :
                        # se o cinema nao estiver lotado ou nao estiver com apenas um lugar sobrando
                        if(people < (lin*col)-1) :
                            # nova procura por assentos
                            continue

                # o assento estava ocupado. procure novamente
                else :
                    # se o cinema nao estiver lotado ou nao estiver com apenas um lugar sobrando
                    if(people < (lin*col)-1) :
                        # nova procura por assentos
                        continue



            # testando se o assento escolhido esta na ponta direita
            if(intendedColumn == col-1) :
                # testando se o assento esta vazio
                if(cinema[intendedRow][intendedColumn] == 0) :
                    # testando se existe gente sentada imediatamente a sua direita
                    # o teste nao eh valido para cinemas com apenas uma coluna (erro de indice)
                    if(cinema[intendedRow][intendedColumn-1] == 0 and col > 1) :
                        cinema[intendedRow][intendedColumn] = 1
                        
                        seated = True
                        # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                        print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                        latestRow = intendedRow
                        latestColumn = intendedColumn

                    else :
                        # se o cinema nao estiver lotado ou nao estiver com apenas um lugar sobrando
                        if(people < (lin*col)-1) :
                            # nova procura por assentos
                            continue

                # o assento estava ocupado. procure novamente
                else :
                    # se o cinema nao estiver lotado ou nao estiver com apenas um lugar sobrando
                    if(people < (lin*col)-1) :
                        # nova procura por assentos
                        continue



            # else: se o individuo NAO quer sentar nas pontas: quer sentar nas colunas do meio
            else :
                # testando se o assento esta vazio
                if(cinema[intendedRow][intendedColumn] == 0) :
                    # testando se esse assento nao possui nenhum individuo sentado ao lado esquerdo e ao lado direito (L e R)
                    if(cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 0) :
                        cinema[intendedRow][intendedColumn] = 1

                        seated = True
                        # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                        print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                        latestRow = intendedRow
                        latestColumn = intendedColumn

                    # testando se esse assento ja possui apenas um individuo sentado ao lado L XOU R
                    elif((cinema[intendedRow][intendedColumn-1] == 0 and cinema[intendedRow][intendedColumn+1] == 1) or \
                         (cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 0)) :
                        cinema[intendedRow][intendedColumn] = 1

                        seated = True
                        # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                        print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                        latestRow = intendedRow
                        latestColumn = intendedColumn

                    elif((cinema[intendedRow][intendedColumn-1] == 1 and cinema[intendedRow][intendedColumn+1] == 1)) :
                        cinema[intendedRow][intendedColumn] = 1

                        seated = True
                        # adicionando 1 aos indices de fileira e coluna para tornar a saida mais intuitiva ao usuario
                        print('O individuo %d [ticket = %d] sentou no assento da fileira %d e coluna %d' % (people+1, intendedSeat, intendedRow+1, intendedColumn+1))
                        latestRow = intendedRow
                        latestColumn = intendedColumn

                    else :
                        print('O cinema esta lotado. Tente novamente em outra sessao.')
                        
                        

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

import random

# cria uma sala de cinema inicialmente vazia
# o cinema sera um bit array:
# 0 := poltrona cinema[i] vazia
# 1 := poltrona cinema[i] ocupada
def createCinema(dim) :
    return [0] * dim

# funcao que acomoda o individuo na poltrona de fileira e coluna escolhidos
# @param
# cinema := a sala de cinema passada como entrada
# people := qual o individuo (iteravel) que esta escolhendo aquela poltrona
# seated := um flag de controle determinando se o individuo ja sentou
def sitAtTheSeat(cinema, people, intendedSeat, seated=True) :
    cinema[intendedSeat] = 1    # ocupa a poltrona desejada
    seated = True               # altera o estado para o individuo 'people'

    print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
        % (people, intendedSeat))
    latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'

    return cinema, latestSeat

# k pessoas compram seus ingressos para assistir a um filme
# o cinema gerado eh inicialmente vazio
def populateCinema(k, cinema) :
    # a dimensao do cinema unidimensional
    dim = len(cinema)

    # se o numero de individuos comprando ingressos for maior do que
    # o tamanho da sala de cinema, so coloco para dentro da sala os
    # primeiros dim individuos, para dim <= k
    if(k > dim) :
        return populateCinema(dim, cinema)


    # "lazy initialization"
    latestSeat = 0
    sitted = 0     # contador de individuos sentados

    # para cada individuo que comprou seu ingresso
    for people in range(k) :
        # variavel de controle que diz se o individuo de indice people ja se sentou
        seated = False

        # enquanto o individuo nao se sentar, procure a melhor poltrona evitando
        # poltronas adjacentes que ja estejam ocupadas
        while( not seated ) :
            # o individuo escolhe aleatoriamente uma poltrona da sala de cinema
            intendedSeat = random.randint(0, dim-1)

            # testa se a poltrona escolhida esta livre
            if (cinema[intendedSeat] == 0) :

                # testa se a poltrona escolhida esta na EXTREMIDADE DIREITA da sala de cinema
                if (intendedSeat == dim-1) :
                    # testa se a poltrona imediatamente a esquerda esta livre
                    if(cinema[intendedSeat-1] == 0) :
                        # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                        cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                        seated = True               # altera o estado para o individuo 'people'

                        print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                            % (people, intendedSeat))
                        latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'
                        sitted += 1

                    # testa se a poltrona imediatamente a esquerda esta ocupada
                    else :
                        # testa se aquela poltrona disponivel eh a ultima da sala de cinema
                        if (sitted == dim-1) :
                            # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                            cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                            seated = True               # altera o estado para o individuo 'people'

                            print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                                % (people, intendedSeat))
                            latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'
                            sitted += 1

                        # testa se existem mais poltronas disponiveis. se sim, procura novamente
                        elif (sitted < dim-1) :
                            continue

                # testa se a poltrona escolhida esta na EXTREMIDADE ESQUERDA da sala de cinema
                if (intendedSeat == 0) :
                    # testa se a poltrona imediatamente a direita esta livre
                    if(cinema[intendedSeat+1] == 0) :
                        # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                        cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                        seated = True               # altera o estado para o individuo 'people'

                        print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                            % (people, intendedSeat))
                        latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'

                        sitted += 1

                    # testa se a poltrona imediatamente a esquerda esta ocupada
                    else :
                        # testa se aquela poltrona disponivel eh a ultima da sala de cinema
                        if (sitted == dim-1) :
                            # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                            cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                            seated = True               # altera o estado para o individuo 'people'

                            print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                                % (people, intendedSeat))
                            latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'

                            sitted += 1

                        # testa se existem mais poltronas disponiveis. se sim, procura novamente
                        elif (sitted < dim-1) :
                            continue

                # testa se a poltrona escolhida esta no "BLOCO DO MEIO" da sala de cinema
                else :
                    # testa se as duas poltronas adjacentes estao livres
                    if(cinema[intendedSeat-1] == 0 and cinema[intendedSeat+1] == 0) :
                        # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                        cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                        seated = True               # altera o estado para o individuo 'people'

                        print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                            % (people, intendedSeat))
                        latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'

                        sitted += 1

                    # caso contrario, testa se a poltrona exatamente a esquerda XOU
                    # a poltrona exatamente a direita estao livres
                    elif ((cinema[intendedSeat-1] == 1 and cinema[intendedSeat+1] == 0) or \
                          (cinema[intendedSeat-1] == 0 and cinema[intendedSeat+1] == 1) ) :
                        # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                        cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                        seated = True               # altera o estado para o individuo 'people'

                        print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                            % (people, intendedSeat))
                        latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'
                        sitted += 1

                    # testa se ambas as poltronas adjacentes estao ocupadas
                    else :
                        # testa se aquela poltrona disponivel eh a ultima da sala de cinema
                        if (sitted == dim-1) :
                            # sitAtTheSeat(cinema, people, intendedSeat, seated=True)
                            cinema[intendedSeat] = 1    # ocupa a poltrona desejada
                            seated = True               # altera o estado para o individuo 'people'

                            print('O individuo %d [ticket = %d] sentou-se na poltrona.' \
                                % (people, intendedSeat))
                            latestSeat = intendedSeat   # sera necessario guardar o valor final escolhido pelo individuo 'people'
                            sitted += 1

                        # testa se existem mais poltronas disponiveis. se sim, procura novamente
                        elif (sitted < dim-1) :
                            continue

                    

            # se a poltrona escolhida estiver ocupada,
            # realizar nova procura por assentos
            else :
                continue

    return cinema, latestSeat

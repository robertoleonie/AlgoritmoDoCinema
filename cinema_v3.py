import random
import time

# https://stackoverflow.com/questions/592746/how-can-you-print-a-variable-name-in-python
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# https://www.reddit.com/r/learnpython/comments/20ucpj/finding_a_sublist_anywhere_within_a_list/
def isSublist(a, b):
    if len(a) > len(b):
        return False
    for i in range(0, len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False

# este metodo cria uma sala de cinema de tamanho dim
# inicialmente vazia
# @param    capacity := a capacidade da sala de cinema  
# @return   cinema[capacity]
def createCinema(capacity) :
    return [0]*capacity

# imprime a disposicao da sala de cinema
# @param    cinema := a estrutura da sala de cinema
def printCinema(cinema) :
    # print("Sessao = %s. Sala no momento: " % (namestr(cinema, globals())[0]))
    time.sleep(1)
    print(cinema)
    print("\n")

# este metodo acomoda um individuo na poltrona sorteada
# @param cinema         := a estrutura da sala de cinema
# @param intendedSeat   := o indice da poltrona
# @param sitting        := o contador de poltronas ocupadas
# @param freeSeats      := o contador de poltronas disponiveis
def accIndividual(cinema, intendedSeat, sitting, freeSeats, seated_individual=True) :
    cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
    seated_individual = True
    sitting += 1                # incrementa o numero de individuos acomodados
    freeSeats -= 1              # decrementa o numero de poltronas disponiveis

    print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
    time.sleep(1)

# ALGORITMO CLASSICO DE POPULAR UMA SALA DE CINEMA
# @param k      := k individuos adentram a uma sala de cinema
# @param cinema := a estrutura representando a sala de cinema
def populateClassic(k, cinema) :
    capacity = len(cinema)                  # armazena a capacidade da sala do cinema
    
    # se o numero de individuos que compraram ingressos for maior
    # do que a capacidade da sala de cinema, adentram a sala
    # apenas os capacity primeiros
    if (k > capacity) :
        return populateClassic(capacity, cinema)
    
    occupiedSeats = []                      # estrutura auxiliar que guarda os indices das poltronas ja escolhidas
    availableSeats = range(0, capacity)     # estrutura auxiliar que guarda os indices das poltronas disponiveis
    sitting = 0                             # contador de individuos sentados ou poltronas ocupadas
    freeSeats = capacity - sitting          # contador de poltronas livres

    print("SESSAO = %s\n" % (namestr(cinema, globals())[0]).upper())

    # para cada individuo que comprou o seu ingresso :
    for individual in range(k) :
        seated_individual = False           # variavel booleana que diz se o individuo atual ja esta acomodado na poltrona
        attempts = []                       # lista auxiliar que guarda todas as tentativas de acomodacao

        # imprime a disposicao da sala de cinema
        print("Sala no momento: ")
        time.sleep(1)
        print(cinema)
        # printCinema(cinema)

        # enquanto o individuo atual nao se acomodou :
        while (not seated_individual) :

            # testa se nao existem mais poltronas disponiveis na sala de cinema
            if (freeSeats == 0) :
                print("A sala de cinema esta totalmente ocupada. Bom filme a todos.")
                exit(1)
            
            availableSeats = list(set(availableSeats) - set(occupiedSeats))     # descarta-se indices que ja foram preenchidos
            intendedSeat = random.choice(availableSeats)                        # escolhe um numero aleatorio entre 0 e capacity-1
            attempts.append(intendedSeat)
            # print(attempts)

            # testa se a poltrona de indice escolhido esta ocupada
            if (cinema[intendedSeat] == 1) :
                continue                    # tenta escolher uma nova poltrona

            # if (cinema[intendedSeat] == 0) :
            else :
                # testa se existe apenas a poltrona escolhida disponivel na sala de cinema
                if (freeSeats == 1) :
                    cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                    seated_individual = True
                    sitting += 1                # incrementa o numero de individuos acomodados
                    freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                    print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                    time.sleep(1)
                    # accIndividual(cinema, intendedSeat, sitting, freeSeats, seated_individual=True)

                # testa se existe mais de uma poltrona disponivel na sala de cinema
                elif (freeSeats > 1) :
                    # testa se a poltrona escolhida esta na ponta direita (i = 0) da sala de cinema
                    if (intendedSeat == 0) :
                        # testa se nao ha individuos acomodados na poltrona imediatamente ao lado
                        if (cinema[intendedSeat+1] == 0) :
                            cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                            seated_individual = True
                            sitting += 1                # incrementa o numero de individuos acomodados
                            freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                            print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                            time.sleep(1)
                            break
                            # accIndividual(cinema, intendedSeat, sitting, freeSeats, seated_individual=True)

                        # if (cinema[intendedSeat+1] == 1) :
                            # ToDo IMPLEMENT ME!!!

                    # testa se a poltrona escolhida esta na ponta direita (i = capacity) da sala de cinema
                    if (intendedSeat == capacity-1) :
                        # testa se nao ha individuos acomodados na poltrona imediatamente ao lado
                        if (cinema[intendedSeat-1] == 0) :
                            cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                            seated_individual = True
                            sitting += 1                # incrementa o numero de individuos acomodados
                            freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                            print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                            time.sleep(1)
                            break
                            # accIndividual(cinema, intendedSeat, sitting, freeSeats, seated_individual=True)

                        # if (cinema[intendedSeat-1] == 1) :
                            # ToDo IMPLEMENT ME !!!

                    # testa se a poltrona escolhida nao esta em nenhuma das pontas ("meio")
                    else :
                        # testa se nao ha individuos acomodados em nenhum dos dois lados da poltrona escolhida
                        if (cinema[intendedSeat-1] == 0 and cinema[intendedSeat+1] == 0) :
                            cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                            seated_individual = True
                            sitting += 1                # incrementa o numero de individuos acomodados
                            freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                            print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                            time.sleep(1)
                            break
                            # accIndividual(cinema, intendedSeat, sitting, freeSeats, seated_individual=True)

                        # testa se existe exatamente um individuo acomodado do lado esquerdo XOU direito da poltrona escolhida
                        elif ((cinema[intendedSeat-1] == 1 and cinema[intendedSeat+1] == 0) or \
                            (cinema[intendedSeat-1] == 0 and cinema[intendedSeat+1] == 1)) :

                            # testa se existe uma sequencia de duas ou tres poltronas vazias na sala de cinema
                            if (not (isSublist([0,0], cinema))) :
                                cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                                seated_individual = True
                                sitting += 1                # incrementa o numero de individuos acomodados
                                freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                                print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                                time.sleep(1)
                                break
                                # ToDo IMPLEMENT ME !!!

                        # testa se as duas poltronas adjacentes estao ocupadas ao mesmo tempo
                        elif (cinema[intendedSeat-1] == 1 and cinema[intendedSeat+1] == 1) :

                            # testa se as seguintes sequencias de poltronas nao existem na sala de cinema
                            if (not (isSublist([0,0,0], cinema)) and not (isSublist([0,0,1], cinema)) and not (isSublist([0,1,0], cinema)) \
                                and not (isSublist([0,1,1], cinema)) and not (isSublist([1,0,0], cinema)) and not (isSublist([1,1,0], cinema))) :
                                cinema[intendedSeat] = 1    # o individuo se acomoda na poltrona desejada
                                seated_individual = True
                                sitting += 1                # incrementa o numero de individuos acomodados
                                freeSeats -= 1              # decrementa o numero de poltronas disponiveis

                                print("O individuo %d [de ticket inicial %d] se acomodou na poltrona %d.\n" % (individual, attempts[0], intendedSeat))
                                time.sleep(1)
                                break
                                # ToDo IMPLEMENT ME !!!

    return cinema

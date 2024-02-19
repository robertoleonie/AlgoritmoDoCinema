import random, math

# https://www.reddit.com/r/learnpython/comments/20ucpj/finding_a_sublist_anywhere_within_a_list/
def isSublist(a, b):
    if len(a) > len(b):
        return False
    for i in range(0, len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False

def deterministicWC(size:int) :
    if (size <= 0) :
        raise SystemExit(f"ERROR: WC cannot have negative or 0 (zero) urinals!\n")
    
    array = [False] * size
    urinalsInUse = 0
    simTime = 0

    # print(f"\nDETERMINISTIC WC WITH {size} URINALS:\n")

    # Inicializa a busca por "bons mictórios" a partir da extremidade mais à esquerda
    idx = 0
    
    while (True) :
        # print(f"WC state: {array}\n")
        # print("===============================================================\n")

        if (idx == size) :
            # print(f"Closing WC...\n")
            # print(f"Execution time = {simTime}.\n")
            # print("===============================================================\n")
            return simTime

        if (urinalsInUse == math.ceil(size/2)) :
            # print("Half of the totality of urinals is already in use!\n")
            # print(f"Closing WC...\n")
            # print(f"Execution time = {simTime}.\n")
            # print("===============================================================\n")
            return simTime
        
        # print(f"Customer has selected urinal no.{idx+1}.\n")

        if (not array[idx]) :
            # Testa extremidade mais à esquerda do sanitário
            if (idx == 0) :
                if (not array[idx+1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                else :
                    if (not isSublist[False, False]) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1

            # Testa extremidade mais à direita do sanitário
            elif (idx == size-1) :
                if (not array[idx-1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                else :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1

            # Testa para os demais mictórios do sanitário
            else :
                # Testa se existe três mictórios consecutivos livres
                if (not array[idx-1] and not array[idx+1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                
                # Testa se existe exatamente dois mictórios consecutivos livres
                else :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1
                '''
                elif ((not array[idx-1] and array[idx+1]) or \
                        (array[idx-1] and not array[idx+1])) :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1
                else :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1
                '''

        # Avança um mictório à direita e incrementa o tempo de simulação.
        idx += 1
        simTime += 1
            
def deterministicWC_v2(size:int) :
    if (size <= 0) :
        raise SystemExit(f"ERROR: WC cannot have negative or 0 (zero) urinals!\n")
    
    array = [False] * size
    urinalsInUse = 0
    simTime = 0

    # print(f"\nDETERMINISTIC WC V2 WITH {size} URINALS:\n")

    # Inicializa a busca por "bons mictórios" a partir da extremidade mais à esquerda
    idx = 0
    
    while (True) :
        # print(f"WC state: {array}\n")
        # print("===============================================================\n")

        if (idx == size) :
            # print(f"Closing WC...\n")
            # print(f"Execution time = {simTime}.\n")
            # print("===============================================================\n")
            return simTime

        if (urinalsInUse == math.ceil(size/2)) :
            # print("Half of the totality of urinals is already in use!\n")
            # print(f"Closing WC...\n")
            # print(f"Execution time = {simTime}.\n")
            # print("===============================================================\n")
            return simTime
        
        # print(f"Customer has selected urinal no.{idx+1}.\n")

        if (not array[idx]) :
            array[idx] = True
            urinalsInUse += 1

        # Avança um mictório à direita e incrementa o tempo de simulação.
        idx += 2
        simTime += 1

def randomizedWC(size:int) :
    if (size <= 0) :
        raise SystemExit(f"ERROR: WC cannot have negative or 0 (zero) urinals!\n")
    
    array = [False] * size
    urinalsInUse = 0
    simTime = 0

    # print(f"\nRANDOMIZED WC WITH {size} URINALS:\n")

    # Lista os mictórios "bons", sem adjacentes ocupados. 
    # Inicialmente são todos
    goodUrinalsList = [i for i in range(0, size)]

    while (True) :
        # print(f"WC state: {array}\n")
        # print("===============================================================\n")

        idx = random.choice(goodUrinalsList)
        # # print(goodUrinalsList)

        if (urinalsInUse == math.floor(size/2) and \
            (0 not in goodUrinalsList and size-1 not in goodUrinalsList)) or \
            (urinalsInUse == math.ceil(size/2)) :
            # print("Half of the totality of urinals is already in use!")
            # print(f"Closing WC...\n")
            # print(f"Execution time = {simTime}.\n")
            # print("===============================================================\n")
            return simTime
        
        # print(f"Customer has selected urinal no.{idx+1}.\n")

        if (not array[idx]) :
            # Testa extremidade mais à esquerda do sanitário
            if (idx == 0) :
                if (not array[idx+1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                    goodUrinalsList.remove(idx)
                    # Remove o mictório adjacente da lista de "bons" mictórios
                    if (idx+1 in goodUrinalsList) :
                        goodUrinalsList.remove(idx+1)
                else :
                    if (not isSublist[False, False]) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1

            # Testa extremidade mais à direita do sanitário
            elif (idx == size-1) :
                if (not array[idx-1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                    goodUrinalsList.remove(idx)
                    # Remove o mictório adjacente da lista de "bons" mictórios
                    if (idx-1 in goodUrinalsList) :
                        goodUrinalsList.remove(idx-1)

                else :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1
                        goodUrinalsList.remove(idx)

            # Testa para os demais mictórios do sanitário
            else :
                # Testa se existe três mictórios consecutivos livres
                if (not array[idx-1] and not array[idx+1]) :
                    # print(f"Customer currently using urinal no.{idx+1}.\n")
                    array[idx] = True
                    urinalsInUse += 1
                    # Remove o mictório adjacente da lista de "bons" mictórios
                    if (idx-1 in goodUrinalsList) :
                        goodUrinalsList.remove(idx-1)
                    if (idx+1 in goodUrinalsList) :
                        goodUrinalsList.remove(idx+1)
                
                # Testa se existe exatamente dois mictórios consecutivos livres
                else :
                    if (not isSublist([False, False], array)) :
                        # print(f"Customer currently using urinal no.{idx+1}.\n")
                        array[idx] = True
                        urinalsInUse += 1

        # Incrementa o tempo de simulação.
        simTime += 1

# detSimTime = deterministicWC(5)
# randSimTime = randomizedWC(5)
        
detSimTime, detSimTime_v2, randSimTime = (0, 0, 0)
for i in range(100000) :
    detSimTime += deterministicWC(5)
    detSimTime_v2 += deterministicWC_v2(5)
    randSimTime += randomizedWC(5)

detSimTime /= 100000
detSimTime_v2 /= 100000
randSimTime /= 100000

print(f"Tempo médio de execução determinístico = {detSimTime}.\n")
print(f"Tempo médio de execução determinístico v2 = {detSimTime_v2}.\n")
print(f"Tempo médio de execução randomizado = {randSimTime}.\n")
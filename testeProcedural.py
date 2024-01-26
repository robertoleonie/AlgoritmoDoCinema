import random, time

class WC :
    def _output(self, txt) :
        txt = str(txt)
        print(txt)
        self._file.write(txt)

    def __init__(self, size : int) :
        if (size <= 0) :
            raise SystemExit(f"ERROR: WC cannot have negative or 0 (zero) urinals!\n")

        self._file = open("output.txt", "w")

        self._size = size
        self._array = [False] * self._size
        
        # Array com os tempos de utilização de mictório
        # self._timeArray = [0] * self._size

        self._urinalsInUse = 0
        self._simTime = 0

        self._output(f"WC successfully created with {self._size} urinals.\n")
        self._output(f"\nWC state: {self._array}\n")
        
        if (self._size > 2) :
            self._freeNeighborhood = [1] + [2] * (self._size - 2) + [1]
            self._neighborhood = [0] * self._size

            # self._output(f"\nWC neighborhood: {self._neighborhood}\n")
            self._output(f"WC free neighborhood: {self._freeNeighborhood}\n")
        self._output("===============================================================\n")

    def _attrUrinal(self, idx : int) :
        if (not self._array[idx]) :
            self._array[idx] = True
            self._urinalsInUse += 1
            self._output(f"Customer using urinal no.{idx+1}.\n")

            if (self._size > 2) :
                if (idx == 0 and self._freeNeighborhood[idx+1] > 0) :
                    self._freeNeighborhood[idx+1] -= 1
                elif (idx == self._size - 1 and self._freeNeighborhood[idx-1] > 0) :
                    self._freeNeighborhood[idx-1] -= 1
                elif (self._freeNeighborhood[idx-1] > 0 and self._freeNeighborhood[idx-1] > 0) :
                    self._freeNeighborhood[idx-1] -= 1
                    self._freeNeighborhood[idx+1] -= 1

                self._neighborhood[0] = 1 - self._freeNeighborhood[0]
                self._neighborhood[1:self._size - 1] = \
                    [2 - x for x in self._freeNeighborhood[1:self._size - 1]]
                self._neighborhood[self._size - 1] = 1 - self._freeNeighborhood[self._size - 1]            
        
    def _testLeftWing(self, idx : int) :
        # Testa o urinal mais à esquerda do sanitário.
        if (idx == 0) :
            # Testa a vizinhança do urinal.
            if (self._array[idx+1]) :
                # Procura algum outro mictório disponível que tenha
                # a vizinhança totalmente livre
                self._countInfreeNeighborhoodAdjFree(idx)
            else :
                self._attrUrinal(idx)

    def _testRightWing(self, idx : int) :
        # Testa o urinal mais à direita do sanitário.
        if (idx == self._size - 1):
            # Testa a vizinhança do urinal.
            if (self._array[idx-1]) :
                # Procura algum outro mictório disponível que tenha
                # a vizinhança totalmente livre
                self._countInfreeNeighborhoodAdjFree(idx)
            else :
                self._attrUrinal(idx)

    def _prioritizeEnds(self, idx : int) :
        if (idx <= self._size // 2) :
            # Priorizar as pontas ao selecionar outro mictório.
            if (not self._array[0]) :
                return 0
            elif (not self._array[self._size - 1]) :
                return self._size - 1
            
            # Sem pontas disponíveis.
            else :
                return -1
            
        else :
            # Priorizar as pontas ao selecionar outro mictório.
            if (not self._array[self._size - 1]) :
                return self._size - 1
            elif (not self._array[0]) :
                return 0
            # Sem pontas disponíveis
            else :
                return -1

    def _countInfreeNeighborhoodAdjFree(self, idx : int) :
        # Procura algum outro mictório disponível que tenha
        # a vizinhança totalmente livre
        twoAdjList = [i for i, n in enumerate(self._freeNeighborhood) \
                      if not self._array[i] and n == 2]
        oneAdjList = [i for i, n in enumerate(self._freeNeighborhood) \
                      if not self._array[i] and n == 1]
        zeroAdjList = [i for i, n in enumerate(self._freeNeighborhood) \
                      if not self._array[i] and n == 0]
        
        # Testa se existem mictórios adjacentes com um ao lado ocupado
        # para evitar novas escolhas.
        consec = 0
        for i in range(0, len(oneAdjList)-2) :
            if (oneAdjList[i] == oneAdjList[i+1] - 1) :
                consec += 1
            consec = 0

        if (len(oneAdjList) == 2 and consec == 1) :
            # self._output("if (len(oneAdjList) == 2 and consec) :\n")
            self._attrUrinal(idx)

        elif (len(twoAdjList) > 0) :
            # self._output("len(twoAdjList) > 0\n")
            # self._output("Selecting another urinal... (1)\n")
            self._output("Selecting another urinal...\n")
            # time.sleep(1)
            # Escolhendo o mictório mais próximo
            closest = min(twoAdjList, key=lambda x : abs(idx - x))
            # idx = random.choice(twoAdjList)
            self._attrUrinal(closest)

        # Se só existe um mictório livre com um adjacente ocupado
        # (o que já foi escolhido), não faz sentido ter que trocar.
        # Se existem ate 2 mictórios consecutivos com um adjacente ocupado,
        # não faz sentido trocar de mictório.
        elif (len(oneAdjList) > 1 and consec < 1) :
            # self._output("elif (len(oneAdjList) > 1 and not consec) :\n")
            # time.sleep(1)
            idxNew = random.choice(oneAdjList)
            idxCand = self._prioritizeEnds(idx)
            if (idxCand != -1) :
                # self._output("Selecting another urinal... (2)\n")
                self._output("Selecting another urinal...\n")
                self._attrUrinal(idxCand)
            else :
                if (idx != idxNew or idx != idxCand) :
                    if (idx in oneAdjList and not(idx == 0 or idx == self._size-1)) :
                        # self._output("Selecting another urinal... (7)\n")
                        self._output("Selecting another urinal...\n")
                self._attrUrinal(idx)

        # Se só existe mictórios livres com um adjacentes ocupados,
        # não faz sentido ter que trocar.
        elif ((idx == 0 or idx == self._size - 1) or len(zeroAdjList) > 1) :
            # self._output("elif ((idx == 0 or idx == self._size - 1) or len(zeroAdjList) > 1) :\n")
            # time.sleep(1)
            idxCand = self._prioritizeEnds(idx)

            if (idx not in zeroAdjList and \
                (0 in zeroAdjList or self._size - 1 in zeroAdjList)) :
                if (idx != idxCand) :
                    # self._output("Selecting another urinal... (6)\n")
                    self._output("Selecting another urinal...\n")
                self._attrUrinal(idxCand)
            else :
                if (idxCand != -1 and (idx > 0 and idx < self._size - 1)) :
                    # self._output("Selecting another urinal... (4)\n")
                    if (idx != idxCand) :
                        self._output("Selecting another urinal...\n")
                    self._attrUrinal(idxCand)
                elif (idxCand == -1) :
                    self._attrUrinal(idx)

        # Se ainda tiver que buscar mictórios com um adjacente ocupado, 
        # opta por buscar mictórios das pontas.
        # Se o mictório previamente escolhido já estiver em uma das pontas,
        # não faz sentido procurar por outro mictório.
        elif (not(idx == 0 or idx == self._size - 1)) :
            # self._output("elif (not(idx == 0 or idx == self._size - 1)) :\n")
            if (idx <= self._size // 2) :
                self._testLeftWing(idx)
                self._testRightWing(idx)
            else :
                self._testRightWing(idx)
                self._testLeftWing(idx)
            if (len(zeroAdjList) > 0) :
                idx = random.choice(zeroAdjList)
            self._attrUrinal(idx)

        else :
            # self._output("else :\n")
            self._attrUrinal(idx)

    def _enterWC(self, idx : int) :
        self._output(f"A customer has entered in the WC.\n")
        self._output(f"Urinal no.{idx+1} chosen.\n")

        if (self._urinalsInUse == self._size) :
            self._output(f"ERROR: WC currently working at full capacity. Please try later.\n")
            return

        if (self._array[idx]) :
            self._output(f"ERROR: Urinal already in use. Please, select another urinal.\n")
            return
        
        if (self._size == 1 or self._size == 2) :
            self._attrUrinal(idx)
        
        else :
            if (idx > 0 and idx < self._size - 1) :
                # Testa os demais urinais do sanitário ("meio").
                # Testa a vizinhança do urinal.
                if (not self._array[idx-1] and not self._array[idx+1]) :
                    self._attrUrinal(idx)
                else :
                    self._countInfreeNeighborhoodAdjFree(idx)
            else :
                if (idx <= self._size // 2 ) :
                    self._testLeftWing(idx)
                    self._testRightWing(idx)
                else :
                    self._testRightWing(idx)
                    self._testLeftWing(idx)

    def _leaveWC(self, idx) :
        if (self._array[idx]) :
            self._array[idx] = False
            self._urinalsInUse -= 1
            self._output(f"Customer has left urinal no.{idx+1}.\n")
            
            if (self._size > 2) :
                if (idx == 0 and self._freeNeighborhood[idx+1] < 2) :
                    self._freeNeighborhood[idx+1] += 1
                elif (idx == self._size - 1 and self._freeNeighborhood[idx-1] < 2) :
                    self._freeNeighborhood[idx-1] += 1
                elif (self._freeNeighborhood[idx-1] < 2 and self._freeNeighborhood[idx-1] < 2) :
                    self._freeNeighborhood[idx-1] += 1
                    self._freeNeighborhood[idx+1] += 1

                self._neighborhood[0] = 1 - self._freeNeighborhood[0]
                self._neighborhood[1:self._size - 1] = \
                    [2 - x for x in self._freeNeighborhood[1:self._size - 1]]
                self._neighborhood[self._size - 1] = 1 - self._freeNeighborhood[self._size - 1] 

        else :
            # O programa deve evitar encerrar o sanitário logo no início
            # de sua execução.
            if (self._simTime > 0 and self._urinalsInUse == 0) :
                self._output("WC is empty!\n")
                self._closeWC()
                return
            else :
                self._output(f"ERROR: Cannot free the urinal no.{idx+1}. It's already empty!\n")
                return

    def _closeWC(self) :
        # Encerra o simulador que está chamando esta função.
        self._output("The WC is closing...\n")
        self._output("WC successfully closed.\n")
        quit()

    def _simulate(self) :
        # 1: Entra no mictório. 2: Sai do mictório
        myDictFunction = { 1 : self._enterWC, 
                            2 : self._leaveWC }

        while True :
            self._output("\n===============================================================\n")
            self._output(f"TIME: {self._simTime}\n")

            # Escolhe aleatoriamente um mictório.
            idx = random.randint(0, self._size-1)

            # Garante que a primeira operação do simulador será de sair do mictório
            if (self._simTime == 0) :
                self._enterWC(idx)
            else :
                option = random.randint(1, 2)
                myDictFunction[option](idx)

            self._output(f"Urinals in use: {self._urinalsInUse}")
            if (self._urinalsInUse == self._size) :
                self._output(" (full)")
            self._output(".\n")

            self._output(f"\nWC state: {self._array}\n")

            if (self._size > 2) :
                # self._output(f"\nWC neighborhood: {self._neighborhood}")
                self._output(f"WC free neighborhood: {self._freeNeighborhood}\n")
            self._output("===============================================================\n")

            self._simTime += 1

size = int(input("Please, enter the number of urinals in the WC: "))
wc = WC(size)
wc._simulate()
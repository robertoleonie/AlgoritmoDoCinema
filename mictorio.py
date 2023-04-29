import time
from random import randrange

mictorios = []
pessoasUrinando = 0

lacos = 0

# n = numero fixo de mictorios do banheiro
def criaBanheiro(n):
    for i in range(0, n):
        mictorios.append(False)    # inicializando com os mictorios vazios
    print("Banheiro criado com os mictorios inicialmente vazios.\n")
    pessoasUrinando = 0
    time.sleep(2)                   # espera 1 segundo



def entraBanheiro(i, tamBanheiro):
    # print(mictorios)
    print("Cliente %d entrou no banheiro." % (i+1))
    time.sleep(1)

    global pessoasUrinando

    if(pessoasUrinando == tamBanheiro):
        print("O banheiro esta lotado. Favor aguardar.")
        exit(1)

    # print(pessoasUrinando)

    elif(pessoasUrinando < tamBanheiro):
        # testar a ponta esquerda do banheiro
        if(i == 0):
            if(mictorios[i] == False):
                if(mictorios[i+1] == False):
                    print("Cliente urinando no mictorio %d..." % (i+1))
                    pessoasUrinando = pessoasUrinando+1
                    mictorios[i] = True
                    time.sleep(2)
                else:
                    if(pessoasUrinando >= tamBanheiro/2):
                        print("Cliente urinando no mictorio %d..." % (i+1))
                        pessoasUrinando = pessoasUrinando+1
                        mictorios[i] = True
                        time.sleep(2)
                    else :
                        print("Procure outro mictorio para urinar.")
            else :
                print("Procure outro mictorio para urinar!")
                saiBanheiro(i, tamBanheiro)

        # testar a ponta direita do banheiro
        elif(i == tamBanheiro-1):
            if(mictorios[i] == False):
                if(mictorios[i-1] == False):
                    print("Cliente urinando no mictorio %d..." % (i+1))
                    pessoasUrinando = pessoasUrinando+1
                    mictorios[i] = True
                    time.sleep(2)
                else:
                    if(pessoasUrinando >= tamBanheiro/2):
                        print("Cliente urinando no mictorio %d..." % (i+1))
                        pessoasUrinando = pessoasUrinando+1
                        mictorios[i] = True
                        time.sleep(2)
                    else :
                        print("Procure outro mictorio para urinar.")
            else :
                print("Procure outro mictorio para urinar!")
                saiBanheiro(i, tamBanheiro)

        # nao esta em nenhuma das pontas
        else :
            if(mictorios[i] == False):               
                if(mictorios[i+1] == False and mictorios[i-1] == False):
                    print("Cliente urinando no mictorio %d..." % (i+1))
                    pessoasUrinando = pessoasUrinando+1
                    mictorios[i] = True
                    # time.sleep(1)
                else :
                    if(pessoasUrinando >= tamBanheiro/2):
                        print("Cliente urinando no mictorio %d..." % (i+1))
                        pessoasUrinando = pessoasUrinando+1
                        mictorios[i] = True
                        # time.sleep(1)
                    else :
                        print("Procure outro mictorio para urinar.")

            else :
                print("Procure outro mictorio para urinar!")
                saiBanheiro(i, tamBanheiro)



def saiBanheiro(i, tamBanheiro):
    # print(mictorios)
    global pessoasUrinando
    global lacos

    if(mictorios[i] == False):
        print("Operacao invalida (saiBanheiro())")
        return

    if(lacos > 0):
        if(pessoasUrinando > 0 and mictorios[i] == True):
            print("\nMictorio (do cliente) %d liberado..." % (i+1))
            mictorios[i] = False
            pessoasUrinando = pessoasUrinando-1
            # time.sleep(1)
            # exit(1)
        if(pessoasUrinando == 0):
            print("\nErro: Banheiro esta vazio!")
            fechaBanheiro(tamBanheiro)
            return



def fechaBanheiro(tamBanheiro):
    global mictorios
    
    cont = 0
    if(pessoasUrinando == 0):
        for i in range(0, tamBanheiro):
            if(mictorios[i] == False) :
                cont = cont+1
        if(cont == tamBanheiro):
            print("O banheiro esta sendo fechado.")
            time.sleep(2)
        exit(1)



def imprimeMictorioBool(tamBanheiro) :
    global mictorios

    micBool = [0] * tamBanheiro
    
    for i in range(0, len(mictorios)):
        if(mictorios[i] == True):
            micBool[i] = 1

    return micBool

def main(tamBanheiro) :
    # tamBanheiro = eval(input("Entre com o numero de mictorios: "))
    criaBanheiro(tamBanheiro)

    global lacos
    global mictorios

    while(True):
        # mic = 0 aborta o programa
        # a escolha do mictorio esta sendo feita de forma aleatoria
        mic = randrange(1,tamBanheiro-1)
        print("Mictorio escolhido: %d" % mic)

        if(mic <= 0 or mic > tamBanheiro) :
            print("Mictorio nao existente.")
            exit(-1)
        
        entraBanheiro(mic-1, tamBanheiro)

        lacos = lacos+1
        print('\n')
        print(mictorios)
        print(imprimeMictorioBool(tamBanheiro))
        print('\n')

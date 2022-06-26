import random

def getFace(var):
    if var == 1:
        return "c"
    else:
        return "k"

def getRandom():
    return random.randint(0,1)

def getPadrao(maxJogadas):
    jogadas = ""
    rand = -1
    face = ""
    
    i=0
    while (i < maxJogadas):
        rand = getRandom()
        face = getFace(rand)
        jogadas+=face
        i+=1
    return jogadas


def getJogadaPlayer(lenght, vez, numJogador):
    jogada = input(f"\nJogador {numJogador} - Digite a sua jogada no formato: j1,j2,...,jn\n")

    if jogada == "exit":
        print("\nVocê fechou o simulador\n")
        exit(1)

    if len(jogada) != lenght:
        print("\nEntrada de dados inválida.Tente novamente.\n")
        vez+=1
        if vez > 3:
            print("\nNúmero de tentativas ultrapassado\n")
            exit(1)
        else:
            getJogadaPlayer(lenght, vez, numJogador)

    else:
        return jogada


def getMaxJogadas():
    nJogadas = int(input("\nDigite a quatidade máxima de jogadas:\n"))

    if nJogadas == -1:
        print("\nVocê fechou o simulador\n")
        exit(1)

    return nJogadas


def getCombInPadrao(padrao, jogadaPlayer):

    if jogadaPlayer in padrao:
        return True
    else:
        return False 


# def getProb(acertos, nJogadas):
#     return acertos/nJogadas


# def comparacaoProb(prob1, prob2):
    
#     print(f"\n-----> CONCLUSÃO:\n\nPlayer 1: {prob1}\nPlayer 2: {prob2}\n")
#     if prob1 > prob2:
#         print("Player 1 tem uma probalidade maior de ganhar")
#         print("Player 2 tem uma probalidade maior de perder\n\n")
#     elif prob1 < prob2:
#         print("Player 2 tem uma probalidade maior de ganhar")
#         print("Player 1 tem uma probalidade maior de perder\n\n")
#     else:
#         print("Player 1 e Player 2 têm a mesma probabilidade de ganhar\n\n")


def main():

    # get numero jogadas
    nJogadas = getMaxJogadas()
    lenght = nJogadas + (nJogadas - 1)

    # player -> OK
    vez = 0
    jogada1 = getJogadaPlayer(nJogadas, vez, 1)
    jogada2 = getJogadaPlayer(nJogadas, vez, 2)

    # Padrão -> OK
    padrao = getPadrao(nJogadas)

    print(getCombInPadrao(padrao, jogada1))
    print(getCombInPadrao(padrao, jogada2))

    # get probabilidade de ganhar
    # prob1 = getProb(acertosP1, nJogadas)
    # prob2 = getProb(acertosP2, nJogadas)

    # comparacaoProb(prob1, prob2)


    return 

main()
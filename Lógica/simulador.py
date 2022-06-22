import random

def getFace(var):
    if var == 1:
        return "c"
    else:
        return "k"

def getRandom():
    return random.randint(0,1)

def getPadrão(maxJogadas):
    jogadas = []
    rand = -1
    face = ""
    
    i=0
    while (i < maxJogadas):
        rand = getRandom()
        face = getFace(rand)
        jogadas.append(face)
        i+=1
    return jogadas


def getJogadaPlayer(maxJogadas, vez, numJogador):
    jogada = input(f"\nJogador {numJogador} - Digite a sua jogada no formato: j1,j2,...,jn\n")

    if jogada == "exit":
        print("\nVocê fechou o simulador\n")
        exit(1)

    if len(jogada) != maxJogadas:
        print("\nEntrada de dados inválida.Tente novamente.\n")
        vez+=1
        if vez > 3:
            print("\nNúmero de tentativas ultrapassado\n")
            exit(1)
        else:
            getJogadaPlayer(maxJogadas, vez)

    else:
        return (jogada.strip()).split(",")


def getMaxJogadas():
    nJogadas = int(input("\nDigite a quatidade máxima de jogadas:\n"))

    if nJogadas == -1:
        print("\nVocê fechou o simulador\n")
        exit(1)

    return nJogadas


def getAcertos(listaPadrao, listaJogadaPlayer):

    acertos = 0
    i = 0
    while (i < len(listaPadrao)):
        if (listaPadrao[i] == listaJogadaPlayer[i]):
            acertos+=1
        i += 1

    return acertos


def getErros(listaPadrao, listaJogadaPlayer):

    erros = 0
    i = 0
    while (i < len(listaPadrao)):
        if (listaPadrao[i] != listaJogadaPlayer[i]):
            erros+=1
        i += 1

    return erros


def getProb(acertos, nJogadas):
    return acertos/nJogadas


def comparacaoProb(prob1, prob2):
    
    print(f"\n-----> CONCLUSÃO:\n\nPlayer 1: {prob1}\nPlayer 2: {prob2}\n")
    if prob1 > prob2:
        print("Player 1 tem uma probalidade maior de ganhar")
        print("Player 2 tem uma probalidade maior de perder")
    elif prob1 < prob2:
        print("Player 2 tem uma probalidade maior de ganhar")
        print("Player 1 tem uma probalidade maior de perder")
    else:
        print("Player 1 e Player 2 têm a mesma probabilidade de ganhar")


def main():

    # get numero jogadas
    nJogadas = getMaxJogadas()
    lenght = nJogadas + (nJogadas - 1)

    # player -> OK
    vez = 0
    lJogada1 = getJogadaPlayer(lenght, vez, 1)
    lJogada2 = getJogadaPlayer(lenght, vez, 2)

    # Padrão -> OK
    padrao = getPadrão(nJogadas)

    # get acertos de cada jogador -> OK
    acertosP1 = getAcertos(padrao, lJogada1)
    acertosP2 = getAcertos(padrao, lJogada2)

    # get probabilidade de ganhar
    prob1 = getProb(acertosP1, nJogadas)
    prob2 = getProb(acertosP2, nJogadas)

    comparacaoProb(prob1, prob2)


    return 

main()
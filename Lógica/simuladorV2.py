import random
import math
import networkx as nx
import matplotlib.pyplot as plt


def getFace(var):
    if var == 1:
        return "c"
    elif var == 0:
        return "k"


def getRandom():
    return random.randint(0, 1)


def getPadrao(maxJogadas):
    jogadas = ""
    rand = -1
    face = ""

    i = 0
    while (i < maxJogadas):
        rand = getRandom()
        face = getFace(rand)
        jogadas += face
        i += 1
    return jogadas


def getJogadaPlayer(lenght, vez, numJogador):
    jogada = input(
        f"\nJogador {numJogador} - Digite a sua jogada no formato: (apenas 0 para k e 1 para c)\n")
    realJogada = ""

    if jogada == "exit":
        print("\nVocê fechou o simulador\n")
        exit(1)
    else:
        i = 0
        while (i < len(jogada)):
            realJogada += getFace(int(jogada[i]))
            i += 1

        if len(realJogada) != lenght:
            print("\nEntrada de dados inválida.Tente novamente.\n")
            vez += 1
            if vez > 3:
                print("\nNúmero de tentativas ultrapassado\n")
                exit(1)
            else:
                getJogadaPlayer(lenght, vez, numJogador)
        else:
            return realJogada


def getMaxJogadas():
    nJogadas = int(input("\nDigite a quatidade máxima de jogadas:\n"))

    if nJogadas == -1:
        print("\nVocê fechou o simulador\n")
        exit(1)

    return nJogadas


def getIndCombInPadrao(padrao, jogadaPlayer, nJogadas):

    i = 0
    while i < len(padrao)-nJogadas-1:
        if jogadaPlayer==padrao[i:i+nJogadas]:
            return i
        i+=1


def getCompJogadas(jog1, jog2, nJogadas, vez, padrao):
    print(f"\nA sequência foi {padrao}.\n")
    if jog1 < jog2:
            print("Jogador 1 venceu e o jogador 2 para a conta.")
    elif jog1 > jog2:
        print("Jogador 2 venceu e o jogador 1 para a conta.")
    elif jog1 == jog2:
        print("\nEmpate. Jogue novamente.\n")
        p1 = getJogadaPlayer(nJogadas, vez, 1)
        p2 = getJogadaPlayer(nJogadas, vez, 2)
        jog1 = getIndCombInPadrao(padrao, p1, nJogadas)
        jog2 = getIndCombInPadrao(padrao, p2, nJogadas)
        vez += 1
        if vez > 10:
            print("\nNúmero de tentativas ultrapassado. Inicie a simulação novamente.\n")
            exit(1)
        else:
            getCompJogadas(jog1, jog2, nJogadas, vez, padrao)


G = nx.DiGraph()


def criaGrafo(sequencia1, sequencia2):

    grafo = {"": {}}

    i = 0

    while sequencia1 not in grafo.keys():

        current_state = sequencia1[:i]

        choice = sequencia1[i:][0]

        next_state = current_state + choice

        grafo[current_state][choice] = next_state

        if next_state not in grafo.keys():
            grafo[next_state] = {}

        i += 1

    i = 0

    while sequencia2 not in grafo.keys():

        current_state = sequencia2[:i]

        choice = sequencia2[i:][0]

        next_state = current_state + choice

        grafo[current_state][choice] = next_state

        if next_state not in grafo.keys():
            grafo[next_state] = {}

        i += 1

    def checkPrevStateExist(origin, state):

        if state == '':
            if 'c' not in grafo[origin].keys():
                grafo[origin]['c'] = ''
            elif 'k' not in grafo[origin].keys():
                grafo[origin]['k'] = ''

        if state not in grafo.keys():
            checkPrevStateExist(origin, state[1:])

        else:
            if 'c' not in grafo[state].keys():
                target_state = (state + 'c')[1:]
                if target_state in grafo.keys():
                    grafo[origin]['c'] = target_state
                else:
                    checkPrevStateExist(origin, target_state[1:])

            elif 'k' not in grafo[state].keys():
                target_state = (state + 'k')[1:]
                if target_state in grafo.keys():
                    grafo[origin]['k'] = target_state
                else:
                    checkPrevStateExist(origin, target_state[1:])

    for state in grafo.keys():

        if state not in [sequencia1, sequencia2]:

            checkPrevStateExist(state, state)

    return grafo


def main():

    # # get numero jogadas
    nJogadas = 3
    nJogadasPadrao = 10*nJogadas

    # # player -> OK
    vez = 0
    jogada1 = getJogadaPlayer(nJogadas, vez, 1)
    jogada2 = getJogadaPlayer(nJogadas, vez, 2)

    # # Padrão -> OK
    padrao = getPadrao(nJogadasPadrao)

    jog1 = getIndCombInPadrao(padrao, jogada1, nJogadas)
    jog2 = getIndCombInPadrao(padrao, jogada2, nJogadas)

    getCompJogadas(jog1, jog2, nJogadas, vez, padrao)

    grafo = (criaGrafo(jogada1, jogada2))

    for node in grafo.keys():
        G.add_node(node)

    plt.figure(2)
    for node in grafo.keys():
        if 'c' in grafo[node].keys():
            G.add_edge(node, grafo[node]['c'])
        if 'k' in grafo[node].keys():
            G.add_edge(node, grafo[node]['k'])

    nx.draw(G, pos=nx.circular_layout(G), with_labels=True)
    plt.show()

    return


main()

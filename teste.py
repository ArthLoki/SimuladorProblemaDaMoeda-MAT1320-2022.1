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


print(criaGrafo('cck', 'ckc'))

#def combinacao_valores(entrada):


def verifica_combinacao(dados:list, valores_teste:list) -> bool:
    # Verifica se uma lista de dados permite parear de forma a atingir o valor teste.

    saida = False

    if len(dados) == 1:
        if dados[0] in valores_teste:
            saida = True
        else:
            saida = False

    for primeiro_dado in range(0, len(dados) - 1):
        for segundo_dado in range(primeiro_dado + 1, len(dados)):
            if dados[primeiro_dado] + dados[segundo_dado] in valores_teste:
                saida = True

    return saida


def proximo_da_combinacao(sequencia: list) -> list:
    if sequencia[0] == sequencia[-1]:
        if sequencia[0] != 6:
            sequencia[0] += 1
            for i in range(1,len(sequencia)):
                sequencia[i] = 1
    else:
        sequencia[1:len(sequencia)] = proximo_da_combinacao(sequencia[1:len(sequencia)])

    return sequencia

def proximo_do_arranjo(sequencia:list)-> list:
    if min(sequencia) != 6:
        if sequencia[0] < 6:
            sequencia[0] += 1
        else:
            sequencia[0] = 1
            sequencia[1:len(sequencia)]  = proximo_do_arranjo(sequencia[1:len(sequencia)])
    return sequencia

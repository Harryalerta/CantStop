def combinar_dados_em_opcoes(lista):
    combinacoes = set()

    combinacoes.add((lista[0] + lista[1],lista[2] + lista[3]))
    combinacoes.add((lista[0] + lista[2],lista[1] + lista[3]))
    combinacoes.add((lista[0] + lista[3],lista[1] + lista[2]))

    return list(combinacoes)
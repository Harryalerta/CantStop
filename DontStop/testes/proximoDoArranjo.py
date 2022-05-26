import modulos.calculadorProbabilidade

lista_anterior = []
lista = [1,1,1,1]

while lista_anterior != lista:
    print(lista)
    lista_anterior = lista.copy()
    lista = modulos.calculadorProbabilidade.proximo_do_arranjo(lista)




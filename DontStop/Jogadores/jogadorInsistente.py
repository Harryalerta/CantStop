from functools import reduce
from modulos.classes import Decisao, Jogador, Tabuleiro


class Jogador_insistente(Jogador):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def decidir(self, valores_possiveis: list, tabuleiro: 'Tabuleiro'):
        self.tabuleiro = tabuleiro
        valor_escolhido =  reduce(lambda valor1, valor2: valor1 if self.avanco_medio(valor1)>=self.avanco_medio(valor2) else valor2, valores_possiveis)
        
        if (len(tabuleiro.lista_colunas_com_marcadores()) == 3):
            deseja_continuar = False
        else:
            deseja_continuar = True

        return Decisao(deseja_continuar,valor_escolhido)

    def posicao_atual(self, coluna: int):
        return self.tabuleiro.colunas[coluna].posicao[self]

    def comprimento_coluna(self, coluna: int):
        return self.tabuleiro.colunas[coluna].comprimento

    def avanco_proporcional(self, coluna: int):
        return self.posicao_atual(coluna)/self.comprimento_coluna(coluna)

    def avanco_medio(self, colunas):
        return sum(map(self.avanco_proporcional, colunas))/len(colunas)



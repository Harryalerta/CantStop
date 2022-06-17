
import copy
from itertools import cycle
import random

from modulos.funcoes import combinar_dados_em_opcoes


class Jogador():
    def __init__(self,nome):
        self.nome=nome

    def decidir(self, valores_possiveis, tabuleiro):
        if (len(tabuleiro.lista_colunas_com_marcadores()) == 3):
            deseja_continuar = False
        else:
            deseja_continuar = True
        for opcao in valores_possiveis:
            if tabuleiro.dados_podem_avancar(opcao):
                return Decisao(deseja_continuar, opcao)


class Decisao():
    def __init__(self,deseja_continuar, valores_escolhidos):
        self.deseja_continuar = deseja_continuar
        self.valores_escolhidos = valores_escolhidos

class Coluna():
    def __init__(self,comprimento, lista_jogadores):
        self.comprimento=comprimento
        self.marcador=0
        self.bloqueado=False

        self.posicao=dict()
        self.posicao[lista_jogadores[0]] = 0
        self.posicao[lista_jogadores[1]] = 0

    def avancar_marcador(self):
        self.marcador+=1

    def gravar_avanco(self,jogador_ativo):
        self.posicao[jogador_ativo] = self.marcador
        self.marcador_reset()
        if self.posicao[jogador_ativo] > self.comprimento:
            self.bloquear_coluna()

    def marcador_reset(self):
        self.marcador = 0

    def marcador_start(self,jogador_ativo):
        self.marcador = self.posicao[jogador_ativo] + 1

    def possui_marcador(self):
        return self.marcador > 0
    
    def bloquear_coluna(self):
        self.bloqueado=True
    
    def esta_bloqueado(self):
        return self.bloqueado

class Tabuleiro():
    def __init__(self, configuracao_jogo):
        self.configuracao_jogo = configuracao_jogo
        self.colunas={}
        for i in range(11):
            self.colunas[i+2] = Coluna(configuracao_jogo.comprimento_colunas[i], configuracao_jogo.lista_jogadores)
    def __str__(self):
        string_retorno = 'Status tabuleiro\n'
        for coluna in self.colunas:
            string_retorno += '[' + str(coluna) + ']' + 'marcador: ' + str(self.colunas[coluna].marcador)
            string_retorno += ' comprimento: ' + str(self.colunas[coluna].comprimento)
            if self.colunas[coluna].esta_bloqueado():
                for jogador in self.configuracao_jogo.lista_jogadores:
                    if self.colunas[coluna].posicao[jogador] > self.colunas[coluna].comprimento:
                        string_retorno += ' - ' + str(jogador.nome) + ' bloqueou'
            else:
                for jogador in self.configuracao_jogo.lista_jogadores:
                    string_retorno += ' - ' + str(jogador.nome) + ' ' + str(self.colunas[coluna].posicao[jogador])
            string_retorno += '\n'
        return string_retorno
    
    def rolar_dados(self):
        return combinar_dados_em_opcoes([random.randrange(1, 7),random.randrange(1, 7),random.randrange(1, 7),random.randrange(1, 7)])

    def lista_colunas_com_marcadores(self):
        return list(filter( lambda coluna : self.colunas[coluna].possui_marcador(), self.colunas))
    
    def lista_colunas_bloqueadas(self):
        return list(filter( lambda coluna : self.colunas[coluna].esta_bloqueado(), self.colunas))

    def limpar_tabuleiro(self):
        for coluna in self.colunas:
            self.colunas[coluna].marcador_reset()

    def gravar_avancos(self , jogador_ativo):
        for coluna in self.lista_colunas_com_marcadores():
            self.colunas[coluna].gravar_avanco(jogador_ativo)

    def pode_adicionar_marcador_na_coluna(self, valor):
        return (valor not in self.lista_colunas_com_marcadores() 
                and valor not in self.lista_colunas_bloqueadas()
                and len(self.lista_colunas_com_marcadores()) < self.configuracao_jogo.quantidade_marcadores)

    def avancar_marcador_coluna(self, valor):
        self.colunas[valor].avancar_marcador()
       
    def start_marcador_coluna(self, valor , jogador_ativo):
        self.colunas[valor].marcador_start(jogador_ativo)

    def valores_podem_avancar(self, valores_possiveis):
        for valores in valores_possiveis:
            if self.dados_podem_avancar(valores):
                return True
        return False

    def dados_podem_avancar(self, dados):
        for valor in dados:
            if (self.pode_adicionar_marcador_na_coluna(valor)
                or self.colunas[valor].possui_marcador()):
                return True
        return False

    def valida_decisao(self, decisao, valores_possiveis):
        if decisao.valores_escolhidos not in valores_possiveis:
            return False
        
        return self.dados_podem_avancar(decisao.valores_escolhidos)

    def executa_decisao(self, decisao, jogador_ativo):
        for valor in decisao.valores_escolhidos:
            if self.pode_adicionar_marcador_na_coluna(valor):
                self.start_marcador_coluna(valor , jogador_ativo)
            elif self.colunas[valor] in self.lista_colunas_com_marcadores():
                self.avancar_marcador_coluna(valor)

        if not decisao.deseja_continuar:
            self.gravar_avancos(jogador_ativo)

    def pode_encerrar(self):
        return len(self.lista_colunas_com_marcadores) < self.configuracao_jogo.quantidade_marcadores

class Configuracao_jogo():
    def __init__(self, quantidade_marcadores , lista_jogadores , comprimento_colunas):
        self.quantidade_marcadores = quantidade_marcadores
        self.lista_jogadores = lista_jogadores
        self.comprimento_colunas = comprimento_colunas


class Gerenciador_partida():
    def __init__(self, configuracao_jogo):
        self.configuracao_jogo = configuracao_jogo

        self.tabuleiro = Tabuleiro(configuracao_jogo)

    def iniciar_jogo(self):
        lista_circular_jogadores = cycle(self.configuracao_jogo.lista_jogadores)
        jogador_ativo = next(lista_circular_jogadores)

        while (len(self.tabuleiro.lista_colunas_bloqueadas()) < 5):
            valores_possiveis = self.tabuleiro.rolar_dados()
            print('---- Inicio da jogada ----')
            print('jogador_ativo')
            print(jogador_ativo.nome)
            
            if self.tabuleiro.valores_podem_avancar(valores_possiveis):
                decisao = jogador_ativo.decidir(valores_possiveis, copy.deepcopy(self.tabuleiro)) ##TODO
                print('decisao.valores_escolhidos')
                print(decisao.valores_escolhidos)

                if (self.tabuleiro.valida_decisao(decisao, valores_possiveis)):
                    self.tabuleiro.executa_decisao(decisao , jogador_ativo)
                    if not decisao.deseja_continuar:
                        print('jogador escolheu encerrar')
                    if self.tabuleiro.pode_encerrar and not decisao.deseja_continuar :
                        print('jogador encerrou')
                        jogador_ativo = next(lista_circular_jogadores)
                else:
                    raise Exception("Valor escolhido não era uma opção")
            else:
                print('jogador perdeu a vez')
                self.tabuleiro.limpar_tabuleiro()
                jogador_ativo = next(lista_circular_jogadores)
            print(self.tabuleiro)
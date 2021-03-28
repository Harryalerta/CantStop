# CantStop
Projeto para contruir uma estrutura que permita pessoas e computadores jogarem Can't Stop

O objetivo real desse projeto é desenvolver as habilidades de programação dos participantes.
    
Para efeitos de padronização, essas são as regras do jogo:
   - Podem participar de 2 a 4 pessoas.
   - A primeira pessoa a jogar é escolhida aleatóriamente.
   - No inicio de cada turno o jogador tem disponível 3 marcadores temporários e deve fazer uma jogada. Uma jogada é o processo de rolar 4 dados de 6 lados, dividí-los em 2 pares de dados da forma que quiser. Chamaremos as somas dos dados de cada dupla de valores da jogada.
   - Para cada valor da jogada, deve-se executar um de duas ações na coluna representada pelo valor da jogada:
       - Adicionar um marcador temporário em coluna disponível.
         - O marcador deve ser colocado na primeira casa da coluna caso não haja um marcador permanente daquele jogador na coluna 
         - e na casa após o marcador permanente caso haja um marcador permanente do jogador na coluna.
       - Avançar um marcador temporário já presente na coluna.
   - Só podem haver 3 marcadores temporários no tabuleiro em qualquer dado momento. Caso já existam 3 marcadores temporários não é possível adicionar um quarto.
   - Caso não seja possível executar nenhuma dessas duas ações, a rodada é perdida e os marcadores temporários são removidos.
   - Caso uma das ações foi executada, escolhe-se entre:
       - Começar um novo turno, mantendo os marcadores temporários da jogada anterior. 
       - Garantir os avanços adquiridos trocando os marcadores temporários por marcadores de avanço permanente do jogador.
   -No momento que um jogador consegue colocar um marcador permanente na casa final da coluna aquela coluna foi conquistada pelo jogador, todos os marcadores permanentes de outros jogadores naquela coluna são removidos e ela está indisponível para jogadas futuras.
   -Vence o jogador que conquistar 3 colunas.

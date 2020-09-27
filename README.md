# CantStop
Projeto para contruir uma estrutura que permita pessoas jogarem e entenderem melhor jogo Can't Stop utilizando um chatbot do telegram.

O objetivo real desse projeto é desenvolver as habilidades de programação dos participantes. O plano é isso ser feito através da construção das seguintes coisas (numa tentativa de ordem de complexidade):
    - Scripts que permitam quantificar as probabilidades de certas situações do jogo.
    - Criação de uma interface que permite duas pessoas jogarem o jogo numa mesma máquina.
    - Criação de um algoritmo que consiga jogar contra um jogador humano e da interface nessária para isso ser feito.
    - Criação de um chat de telegram para pessoas jogarem o jogo em um grupo de conversa.
    - Criação de uma API para que pessoas possam criar inteligências artificiais para participarem de um jogo e que IAs possam ser colocada para jogar entre si.
    
Para efeitos de padronização, essas são as regras do jogo:
   - Podem participar de 2 a 4 pessoas.
   - A primeira pessoa a jogar é escolhida aleatóriamente.
   - No inicio de seu turno, deve-se rolar 4 dados de lados, combiná-los em 2 pares de dados da forma que quiser e somar seus valores. Chamaremos esses 2 valores de valores da jogada.
   - Para cada valor da jogada, deve-se executar um de duas ações:
       - Adicionar um marcador temporário na coluna respectiva do valor da jogada na primeira casa.
       - Avançar um marcador temporário já presente na coluna.
   - Só podem haver 3 marcadores temporários no tabuleiro em qualquer dado momento. Caso já existam 3 marcadores temporários não é possível adicionar um quarto e a opção não está disponível.
   - Caso não seja possível executar nenhuma dessas duas ações, a rodada é perdida e os marcadores temporários são removidos.
   - Caso uma das ações foi executada, escolhe-se entre:
       - Começar um novo turno, mantendo os marcadores temporários da rodada anterior. 
       - Garantir os avanços adquiridos trocando os marcadores temporários por marcadores de avanço permanente do jogador.
   - Em rodadas subsequentes um marcador temporário, quando adicionado numa coluna onde já houver um marcador de avanço permanente, deve ser colocado na casa seguinte ao marcador permanente.
   [TO DO} descrever o tabuleiros e as mecânicas de fim de jogo.

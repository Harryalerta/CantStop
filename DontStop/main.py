from modulos.classes import Jogador, Configuracao_jogo, Gerenciador_partida
from Jogadores.jogadorInsistente import Jogador_insistente

comprimento_colunas = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
lista_jogadores = [Jogador('Pla'), Jogador_insistente('Gustavo')]

configuracao_jogo = Configuracao_jogo(3, lista_jogadores, comprimento_colunas)

gerenciador = Gerenciador_partida(configuracao_jogo)

vencedores = []
for i in range(500):
    vencedores.append(gerenciador.iniciar_jogo())

print('fim')
print(lista_jogadores[0].nome + ' venceu '+ str(vencedores.count(lista_jogadores[0]))+ ' vezes')    
print(lista_jogadores[1].nome + ' venceu '+ str(vencedores.count(lista_jogadores[1]))+ ' vezes')    


# pygame.font.init()
# pygame.mixer.init()

# WIDTH, HEIGHT = 900, 500
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("First Game!")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)

# BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
# WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# FPS = 60


# def draw_window():
#     pygame.draw.rect(WIN, BLACK, BORDER)


#     pygame.display.update()

# def main(configuracao_jogo):


#     red_bullets = []
#     yellow_bullets = []

#     red_health = 10
#     yellow_health = 10
#     comprimento_colunas = [2,4,6,8,10,12,10,8,6,4,2]
#     lista_jogadores = [Jogador('Gustavo'), Jogador('Pla')]

#     configuracao_jogo = Configuracao_jogo( 3, lista_jogadores , comprimento_colunas)

#     gerenciador = Gerenciador_partida(configuracao_jogo)
#     lista_circular_jogadores = cycle(configuracao_jogo.lista_jogadores)
#     jogador_ativo = next(lista_circular_jogadores)
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()

#         keys_pressed = pygame.key.get_pressed()
#         draw_window()


#     main()
# if __name__ == "__main__":
#     main()

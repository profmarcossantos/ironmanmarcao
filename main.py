import pygame
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Iron Man do Marcão")
branco = (255,255,255)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill(branco)
    pygame.display.update()
    relogio.tick(60)

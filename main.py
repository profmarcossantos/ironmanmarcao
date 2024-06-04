import pygame
import random
import os
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Iron Man do Marcão")
icone  = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
branco = (255,255,255)
preto = (0, 0 ,0 )
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXPersona  = 0
movimentoYPersona  = 0
posicaoXMissel = 400
posicaoYMissel = -240
velocidadeMissel = 1
missileSound = pygame.mixer.Sound("assets/missile.wav")
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
pygame.mixer.Sound.play(missileSound)
fonte = pygame.font.SysFont("comicsans",28)
fonteMorte = pygame.font.SysFont("arial",120)

pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)
pontos = 0
larguraPersona = 250
alturaPersona = 127
larguaMissel  = 50
alturaMissel  = 250
dificuldade  = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = -10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = -10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = 10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0
            
    posicaoXPersona = posicaoXPersona + movimentoXPersona            
    posicaoYPersona = posicaoYPersona + movimentoYPersona            
    
    if posicaoXPersona < 0 :
        posicaoXPersona = 10
    elif posicaoXPersona >550:
        posicaoXPersona = 540
        
    if posicaoYPersona < 0 :
        posicaoYPersona = 10
    elif posicaoYPersona > 473:
        posicaoYPersona = 463
    
        
    tela.fill(branco)
    tela.blit(fundo, (0,0) )
    #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
    tela.blit( iron, (posicaoXPersona, posicaoYPersona) )
    
    posicaoYMissel = posicaoYMissel + velocidadeMissel
    if posicaoYMissel > 600:
        posicaoYMissel = -240
        pontos = pontos + 1
        velocidadeMissel = velocidadeMissel + 1
        posicaoXMissel = random.randint(0,800)
        pygame.mixer.Sound.play(missileSound)
        
        
    tela.blit( missel, (posicaoXMissel, posicaoYMissel) )
    
    texto = fonte.render("Pontos: "+str(pontos), True, branco)
    tela.blit(texto, (10,10))
    
    pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
    pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
    pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + larguaMissel))
    pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + alturaMissel))
    
    os.system("cls")
    print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
    if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
        if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
            print("Morreuuuuu")
            textoMorte = fonteMorte.render("Morreuuuu", True, preto)
            tela.blit(textoMorte, (200,300))
            pygame.mixer.Sound.play(explosaoSound)

        else:
            print("Ainda Vivo, mas por pouco!")
    else:
        print("Ainda Vivo")
    
    
   
    
    pygame.display.update()
    relogio.tick(60)

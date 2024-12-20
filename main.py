import pygame
import random

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Corrida Maluca")

branco = (255, 255, 255)
preto = (0, 0, 0)
backgroundFinal = ("assets/backgrouond_final.jpg")

fundo = pygame.image.load("assets/fundo.png")
fundo = pygame.transform.scale(fundo, tamanho)
fundo_final = pygame.image.load("assets/background_final.jpg")
fundo_final = pygame.transform.scale(fundo_final, tamanho)
ferrari_vermelha = pygame.image.load("assets/carro1.png")
lamborghini_amarela = pygame.image.load("assets/carro2.png")
porsche_azul = pygame.image.load("assets/carro3.png")

pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1)
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)

movXFerrari = -30
movXLamborghini = -30
movXPorsche = -30
posYFerrari = 30
posYLamborghini = 190
posYPorsche = 110

acabou = False
somDaVitoria = False

ferrari_na_pista_inferior = False
lamborghini_na_pista_inferior = False
porsche_na_pista_inferior = False

fonte = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    tela.fill(branco)
    if not acabou:
        tela.blit(fundo, (0, 0))
    else:
        tela.blit(fundo_final, (0, 0))

    tela.blit(ferrari_vermelha, (movXFerrari, posYFerrari))
    tela.blit(lamborghini_amarela, (movXLamborghini, posYLamborghini))
    tela.blit(porsche_azul, (movXPorsche, posYPorsche))

    if not acabou:
        movXFerrari += random.randint(0, 10)
        movXLamborghini += random.randint(0, 10)
        movXPorsche += random.randint(0, 10)
    else:
        pygame.mixer.music.stop()
        if not somDaVitoria:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True

    if movXFerrari >= 1000 and not ferrari_na_pista_inferior:
        movXFerrari = -30
        posYFerrari = 350
        ferrari_na_pista_inferior = True

    if movXLamborghini >= 1000 and not lamborghini_na_pista_inferior:
        movXLamborghini = -30
        posYLamborghini = 480
        lamborghini_na_pista_inferior = True

    if movXPorsche >= 1000 and not porsche_na_pista_inferior:
        movXPorsche = -30
        posYPorsche = 420
        porsche_na_pista_inferior = True

    posicoes = sorted([
        (movXFerrari + (1000 if ferrari_na_pista_inferior else 0), "Ferrari Vermelha"),
        (movXLamborghini + (1000 if lamborghini_na_pista_inferior else 0), "Lamborghini Amarela"),
        (movXPorsche + (1000 if porsche_na_pista_inferior else 0), "Porsche Azul")
    ], reverse=True)

    
    distancia1_2 = posicoes[0][0] - posicoes[1][0]
    distancia2_3 = posicoes[1][0] - posicoes[2][0]

   
    distancia1_2_metros = distancia1_2 / 8  
    distancia2_3_metros = distancia2_3 / 8 

    
    texto_ranking = fonte.render(f"1º: {posicoes[0][1]} - Distância para 2º: {distancia1_2_metros:.2f} m", True, preto)
    texto_ranking2 = fonte.render(f"2º: {posicoes[1][1]} - Distância para 3º: {distancia2_3_metros:.2f} m", True, preto)
    tela.blit(texto_ranking, (50, 20))
    tela.blit(texto_ranking2, (50, 60))

    if (ferrari_na_pista_inferior and movXFerrari >= 900) or \
       (lamborghini_na_pista_inferior and movXLamborghini >= 900) or \
       (porsche_na_pista_inferior and movXPorsche >= 900):
        vencedor_texto = fonte.render(f"{posicoes[0][1]} Ganhou!", True, branco)
        tela.blit(fundo_final, (0, 0))  
        tela.blit(vencedor_texto, (270, 70))  
        acabou = True

    pygame.display.update()

    clock.tick(60)
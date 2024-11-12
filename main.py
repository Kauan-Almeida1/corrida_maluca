import pygame
import random

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Corrida Maluca")

branco = (255, 255, 255)
fundo = pygame.image.load("assets/fundo.png")
fundo = pygame.transform.scale(fundo, tamanho)

clock = pygame.time.Clock()
acabou = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    
    pygame.display.update()
    clock.tick(60)

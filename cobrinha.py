import pygame
from sys import exit
from random import randint
from pygame.locals import *

pygame.init()
frame = pygame.time.Clock()
pygame.display.set_caption("Jogo da cobrinha")
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

x = altura / 2
y = largura / 2
velocidade = 10
x_controle = velocidade
y_controle = 0
lista_cobra = []

comprimento_inicial = 1
def crescer(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0],XeY[1], 20, 20))

x_m = randint(30, 400)
y_m = randint(30, 400)
ponto = 0
fonte = pygame.font.SysFont("comic sans",40, True, True)

while True:
    tela.fill((0,0,0))
    frame.tick(30)
    mensagem = f"pontos: {ponto}"
    texto = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        if x_controle == velocidade:
            pass
        else:
            x_controle = -velocidade
            y_controle = 0
    if pygame.key.get_pressed()[K_RIGHT]:
        if x_controle == -velocidade:
            pass
        else:
            x_controle = velocidade
            y_controle = 0
    if pygame.key.get_pressed()[K_UP]:
        if y_controle == velocidade:
            pass
        else:
            y_controle = -velocidade
            x_controle = 0
    if pygame.key.get_pressed()[K_DOWN]:
        if y_controle == -velocidade:
            pass
        else:
            y_controle = velocidade
            x_controle = 0
    
    x = x + x_controle
    y = y + y_controle
    
    cobra = pygame.draw.rect(tela, (0,255,0), (x, y, 20, 20))
    maça = pygame.draw.rect(tela, (255,0,0), (x_m, y_m, 20, 20))

    if cobra.colliderect(maça):
        x_m = randint(30, 400)
        y_m = randint(30, 400)
        ponto = ponto + 1
        comprimento_inicial	= comprimento_inicial + 1
  
  
    lista_cabeça = []
    lista_cabeça.append(x)
    lista_cabeça.append(y)

    lista_cobra.append(lista_cabeça)
    if lista_cobra.count(lista_cabeça) > 1:
        break

    crescer(lista_cobra)
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    tela.blit(texto, (440, 40))
    pygame.display.update()
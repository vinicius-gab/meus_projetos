#Importações
import pygame
from sys import exit
from pygame.locals import * 

#iniciar o pygame
pygame.init()

#Variaveis
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Escape Room")
frame = pygame.time.Clock()

#Cores
preto = ((0, 0, 0))
branco = ((255, 255, 255))

#Tela inical
fonte = pygame.font.SysFont("arial", 40, True, True)
mensagem = 'Escape Room'
titulo = fonte.render(mensagem, True, (255, 255, 255))
x_titulo = (largura - titulo.get_width()) // 2
y_titulo = (altura - titulo.get_height()) // 2
iniciar = 'aperte "espaço" para iniciar'
start = fonte.render(iniciar, True, (255, 255, 255))
x_start = (largura - start.get_width()) // 2
y_start = y_titulo + titulo.get_height() + 10
inicio = False
fonte_nome = pygame.font.SysFont("comic sans", 25)

#Sprite

#parte tecnicas

#loop principal
while True:
    tela.fill(preto)
    frame.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(titulo, (x_titulo, y_titulo))
    tela.blit(start, (x_start, y_start))
    if pygame.key.get_pressed()[K_SPACE]:
        tela.fill(preto)
        inicio = True
    if inicio == True:
        tela.fill((preto))
    pygame.display.flip()

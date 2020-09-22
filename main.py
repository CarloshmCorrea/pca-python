import pygame # na primeira linha importamos o pygame e na segunda fizemos rodar
from random import randint
pygame.init() 

x = 400 #Variaveis da posição horizontal e vertical da nave
y = 300

pos_x = 400 #Variaveis das posições dos asteroides
pos_y1 = 0
pos_y2 = 0
pos_y3 = 0

velocidade_nave = 7 #variaveis de velocidade da nave e dos asteroides
velocidade_asteroides = 4

#importações das imagens diversas

fundo = pygame.image.load('data/img/fundo2r.jpg') 
nave = pygame.image.load('data/img/nave.png')
asteroide1 = pygame.image.load('data/img/asteroide1.png')
asteroide2 = pygame.image.load('data/img/asteroide2.png')
asteroide3 = pygame.image.load('data/img/asteroide3.png')

#musicas /sons de efeitos

pygame.mixer.music.load('data/sound/son_fundo.wav')
pygame.mixer.music.play(-1)

janela = pygame.display.set_mode((1280,800)) #tamanho da tela
pygame.display.set_caption("Jogo Tinsinando") #titulo da tela

janela_aberta = True
while janela_aberta:
    pygame.time.delay(5)

    for event in pygame.event.get(): #Loop para tela ficar aberta
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed() #comandos de direção da nave
    if comandos[pygame.K_w]:
        y -= velocidade_nave
    if comandos[pygame.K_s]:
        y += velocidade_nave
    if comandos[pygame.K_a]:
        x -= velocidade_nave
    if comandos[pygame.K_d]:
        x += velocidade_nave
    
    if (pos_y1 > 1280) and (pos_y2 > 1280) and (pos_y3 > 1280): #comandos de loop/surgimentos dos asteroides na vertical
        pos_y1 = randint(-400,-100)
        pos_y2 = randint(-400,-100)
        pos_y3 = randint(-400,-100)
       

    pos_y1 += velocidade_asteroides #rodando a variavel de velocidade dos asteroides
    pos_y2 += velocidade_asteroides #rodando a variavel de velocidade dos asteroides
    pos_y3 += velocidade_asteroides #rodando a variavel de velocidade dos asteroides

    janela.blit(fundo,(0,0)) #sobreposição da imagem do fundo
    janela.blit(nave,(x,y)) #sobreposição da imagem da nave
    janela.blit(asteroide1,(pos_x,pos_y1)) #sobreposição da img do asteroide2
    janela.blit(asteroide2,(pos_x + 450,pos_y2 +450)) #sobreposição da img do asteroide2
    janela.blit(asteroide3,(pos_x + 700,pos_y3 +700)) #sobreposição da img do asteroide3
    pygame.display.update()


pygame.quit()                
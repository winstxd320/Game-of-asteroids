import pygame
import random
pygame.init()
#variables del proyecto
aste_ancho = 50
aste_alto = 50
nave_ancho = 50
nave_alto = 50
ancho = 500
alto = 450
pos_x = 200
pos_y = 400
run = True
vidas = 5
# boton de pausa
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                if event.key == pygame.K_p:
                    run = False
                if event.key == pygame.K_c:
                    run = True
                    paused = False
# texto
fuente = pygame.font.SysFont("Console", 30)
fuente2 = pygame.font.SysFont("Console", 50)

#pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de asteroides")
# asteroidies
asteroides = []
for i in range(5):
    x = random.randint(1, 499)
    y = random.randint(1, 449)
    c = [x, y]
    asteroides.append(c)
while run:
    for event in pygame.event.get():
            # bandera
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pos_x += 40
                if pos_x > 450:
                    pos_x = 449
            if event.key == pygame.K_LEFT:
                pos_x -= 40
                if pos_x < 0:
                    pos_x = 1
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_c:
                pause()
            if event.key == pygame.K_r:
                for c in asteroides:
                    vidas = 5
                    pos_x = 200
                    pos_y = 400
                    c[0] = random.randint(1, 499)
                    c[1] = random.randint(1, 449)
                    pygame.display.update()
        # animación    de asteroides
    for c in asteroides: # posición de las animaciones
        c[0] += 1
        c[1] += 2
        if c[0] > ancho:
            c[0] = -50
        if c[1] > alto:
            c[1] = -50
    pantalla.fill((0, 0, 0))
        # nave
    nave = pygame.draw.rect(pantalla, (0, 255, 0), (pos_x, pos_y, nave_ancho, nave_alto))
        # asteroide
    for c in asteroides:
        aste = pygame.draw.rect(pantalla, (255, 255, 255), (c[0], c[1], aste_ancho, aste_alto))
        if aste.colliderect(nave):
            vidas -= 1
            pos_x = 200
            pos_y = 400
            c[0] = random.randint(1, 499)
            c[1] = random.randint(1, 449)
        if vidas == 0:
            pos_x = 1000000
            c[0] = 1000000
            c[1] = 1000000
            texto2 = fuente2.render("GAME OVER", True, (255, 255, 255))
            pantalla.blit(texto2, (115, 200))

    texto = fuente.render("Vidas: " + str(vidas),  True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))
    pygame.display.update()
    pygame.time.delay(7)
pygame.display.quit()
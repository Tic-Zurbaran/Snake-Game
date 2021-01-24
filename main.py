# Librerias importadas
import pygame as pg
import sys, random, time
from pygame.locals import *
import constants as c


# Iniciar pygame
pg.init()

# Ventana 
screen = pg.display.set_mode(c.size)

# FPS
clock = pg.time.Clock()
clock.tick(c.fps)

# Imágenes
manzana = pg.image.load("manzana.png")
background = pg.image.load("bg.png")
# Título
pg.display.set_caption("Snake Game")

# Posicion Inicial 
player_x, player_y = c.x[c.x_P], c.y[c.y_P]
old_player_x, old_player_y = player_x, player_y

player_y_old, player_x_old = player_y, player_x


manzana_x, manzana_y = random.choice(c.x), random.choice(c.y)

punto =0


# Bucle de juego
while True:

	# Salida del juego
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		
		# Keyboard
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				c.direccion = "up"

			if event.key == pg.K_DOWN:
				c.direccion = "down"

			if event.key == pg.K_LEFT:
				c.direccion = "left"

			if event.key == pg.K_RIGHT:
				c.direccion = "right"





	# Color de fondo
	screen.fill(c.dark_olive)
	screen.blit(background, (-3, 0))



	# Lineas Verticales
	#for i in range(10, 1280, 30):
	#	pg.draw.line(screen, c.white, [i, 10], [i, 700], 1)

	# Lineas Horizontales
	#for i in range(10, 720, 30):
	#	pg.draw.line(screen, c.white, [10, i], [1270, i], 1)

	# Manzana 
	screen.blit(manzana, (manzana_x,manzana_y))


	#Puntos 
	if player_y == manzana_y and player_x == manzana_x:
		manzana_x, manzana_y = random.choice(c.x), random.choice(c.y)
		punto +=1
		cpoint = c.point
		cpoint.append(punto)

		print(c.point)



	## Movimiento ##

	# Movimiento hacia arriba
	if c.y_P > 0:
		if c.direccion == 'up':
			 old_player_y= player_y
			 player_y = c.y[c.y_P-1]
			 c.y_P -= 1 
			 time.sleep(0.05)

	# Movimiento hacia abajo
	if c.y_P < 22:
		if c.direccion == 'down':
			old_player_y= player_y
			player_y = c.y[c.y_P+1]
			c.y_P += 1 
			time.sleep(0.05)

		
	# Movimineto hacia la izquierda
	if c.x_P > 0:
		if c.direccion == 'left':
			old_player_x= player_x
			player_x = c.x[c.x_P-1]
			c.x_P -= 1 
			time.sleep(0.05)
			print(c.x_P)
	
	# Movimiento hacia la derecha 
	if c.x_P < 41:
		if c.direccion == 'right':
			old_player_x= player_x
			player_x = c.x[c.x_P+1]
			c.x_P += 1 
			time.sleep(0.05)
			print(c.x_P)



	# Player
	pg.draw.rect(screen, c.white, (player_x, player_y, 30, 30))

	if len(c.point) > 1:
		if c.direccion == 'up':
			for i in c.point:
				pg.draw.rect(screen, c.white, (player_x, c.y[c.y_P+i] , 30, 30))
				time.sleep(0.05)
		if c.direccion == 'down':
			for i in c.point:
				pg.draw.rect(screen, c.white, (player_x, c.y[c.y_P-i], 30, 30))
				time.sleep(0.05)
		if c.direccion == 'right':
			for i in c.point:
				pg.draw.rect(screen, c.white, (c.x[c.x_P+1], player_y, 30, 30))
				time.sleep(0.05)
		if c.direccion == 'left':
			for i in c.point:
				pg.draw.rect(screen, c.white, (c.x[c.x_P-1], player_y, 30, 30))
				time.sleep(0.05)




	pg.display.flip()










# Librerias importadas
import pygame as pg
import sys, random, time
from pygame.locals import *
import constants as c

mov=0

# Iniciar pygame
pg.init()

# Ventana 
screen = pg.display.set_mode(c.size)

# FPS
clock = pg.time.Clock()
clock.tick(c.fps)
# Imagenes
manzana = pg.image.load("manzana.png")

# Titulo
pg.display.set_caption("Snake Game")

# Posicion Inicial 
player_x, player_y = c.x[c.x_P], c.y[c.y_P]
player_y_old, player_x_old = player_y, player_x


manzana_x, manzana_y = random.choice(c.x), random.choice(c.y)



#pg.draw.rect(screen, c.yellow_green, (c.x[21], c.y[11], 30, 30))

direccion = "nothing"

# Bucle de juego
while True:

	# Salida del juego
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		
		# Keyboard
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				direccion = "up"

			if event.key == pg.K_DOWN:
				direccion = "down"

			if event.key == pg.K_LEFT:
				direccion = "left"

			if event.key == pg.K_RIGHT:
				direccion = "right"





	# Color de fondo
	screen.fill(c.dark_olive)

	# Lineas Verticales
	for i in range(10, 1280, 30):
		pg.draw.line(screen, c.white, [i, 10], [i, 700], 1)

	# Lineas Horizontales
	for i in range(10, 720, 30):
		pg.draw.line(screen, c.white, [10, i], [1270, i], 1)

	# Manzana 

	screen.blit(manzana, (manzana_x,manzana_y))


	#Puntos 

	if player_y == manzana_y and player_x == manzana_x:
		manzana_x, manzana_y = random.choice(c.x), random.choice(c.y)
		c.point +=1
		print(c.point)



	# Logica
	if c.y_P > -1:
		if direccion == 'up':
			 player_y = c.y[c.y_P-1]
			 c.y_P -=1 
			 time.sleep(0.05)


	if c.y_P < 22:
		if direccion == 'down':
			player_y = c.y[c.y_P+1]
			c.y_P +=1 
			time.sleep(0.05)

		

	if direccion == 'left':
		pass

	if direccion == 'right':
		pass



	if c.point>0:

		if direccion == 'up':
			pass


		


	# Player
	pg.draw.rect(screen, c.white, (player_x, player_y, 30, 30))
	



	pg.display.flip()










# Archivo Main donde está el flujo principal del juego, el juego se ejecutará desde este archivo.

# Librerías importadas
import sys, random, time
import pygame as pg # Abreviamos pygame con pg
import constants as c # Abreviamos constantes con c

# Inicia pygame
pg.init()

# Funciones
font_style = pg.font.SysFont("none", 25)
def mensaje(msg, color, posx, posy): # Para mostrar texto por pantalla
	mesg = font_style.render(msg, True, color)
	pantalla.blit(mesg, [posx, posy])

def snake(bloque_snake, lista_snake):
	for x in lista_snake:
		pg.draw.rect(pantalla, c.green_snake, [x[0], x[1], bloque_snake, bloque_snake])

#Pantalla
pantalla = pg.display.set_mode((c.ancho,c.alto)) # Establece propiedades de tamaño a la pantalla

clock = pg.time.Clock() # FPS

pg.display.set_caption('Snake game') # Indica el nombre en la ventana

bg = pg.image.load("imagenes/bg.png")
manzana = pg.image.load("imagenes/manzana.png")
snake_down = pg.image.load("imagenes/snake_down.png")
snake_right = pg.image.load("imagenes/snake_right.png")
snake_up = pg.image.load("imagenes/snake_up.png")
snake_left = pg.image.load("imagenes/snake_left.png")
setup_facil = pg.image.load("imagenes/facil.png")
setup_normal = pg.image.load("imagenes/normal.png")
setup_dificil = pg.image.load("imagenes/dificil.png")
setup_si = pg.image.load("imagenes/si.png")
setup_no = pg.image.load("imagenes/no.png")
setup_bg = pg.image.load("imagenes/setup.png")
game_over = pg.image.load("imagenes/game_over.png")


def bucle_juego(): # Función general del juego
	c.muerte = False
	c.fin = False
	for i in range(1):
		pantalla.blit(setup_bg, (0, 0))

	while c.setup:
		print(c.fps)
		for event in pg.event.get(): # Registra eventos
				if event.type==pg.QUIT: # Registra el evento del botón de salir
					sys.exit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_1 or event.key == pg.K_KP1:
						c.fps = 12
						pantalla.blit(setup_bg, (0, 0))
						pantalla.blit(setup_facil, (960, 175))
					elif event.key == pg.K_2 or event.key == pg.K_KP2:
						c.fps = 22
						pantalla.blit(setup_bg, (0, 0))
						pantalla.blit(setup_normal, (945, 270))	
					elif event.key == pg.K_3 or event.key == pg.K_KP3:
						c.fps = 40 
						pantalla.blit(setup_bg, (0, 0))
						pantalla.blit(setup_dificil, (960, 360))	
					elif event.key == pg.K_6 or event.key == pg.K_KP6:
						c.texturas = False
						pantalla.blit(setup_bg, (0, 0))
						pantalla.blit(setup_no, (1015, 605))
					elif event.key == pg.K_5 or event.key == pg.K_KP5:
						c.texturas = True
						pantalla.blit(setup_bg, (0, 0))
						pantalla.blit(setup_si, (930, 603))
					elif event.key == pg.K_SPACE:
						c.setup = False 

		pg.display.update()

	while not c.fin: # Bucle While que se repetirá hasta que fin = True
		while c.muerte: # Bucle que se ejecuta cuando muerte = True (cuando nos matan)
			pantalla.blit(game_over,(0,0))
			pg.display.update()# Actualiza pantalla
			for event in pg.event.get(): # Registra eventos 
				if event.type == pg.KEYDOWN: # Registra eventos de teclado de espacio y escape
					if event.key == pg.K_ESCAPE: # Espacio
						c.fin = True
						c.muerte = False
					if event.key == pg.K_SPACE: # Escape
						c.snake_x= c.x[21]
						c.snake_y= c.y[12]
						c.largo_snake = 1
						c.lista_snake=[]
						c.snake_x_cambio, c.snake_y_cambio = 0,0


						bucle_juego()


		for event in pg.event.get(): # Registra eventos
			if event.type==pg.QUIT: # Registra el evento del botón de salir
				c.fin=True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT or event.key == pg.K_a:
					c.snake_x_cambio = -c.bloque_snake
					c.snake_y_cambio = 0
				elif event.key == pg.K_RIGHT or event.key == pg.K_d:
					c.snake_x_cambio = c.bloque_snake
					c.snake_y_cambio = 0
				elif event.key == pg.K_UP or event.key == pg.K_w:
					c.snake_y_cambio = -c.bloque_snake
					c.snake_x_cambio = 0
				elif event.key == pg.K_DOWN or event.key == pg.K_s:
					c.snake_y_cambio = c.bloque_snake
					c.snake_x_cambio = 0

		# Movimiento
		c.snake_x += c.snake_x_cambio
		c.snake_y += c.snake_y_cambio

		if c.snake_x >= c.ancho-25 or c.snake_x < 0 or c.snake_y >= c.alto-25 or c.snake_y < 0: # Comprueba si se choca con los límites
			c.muerte = True

		# Objetos
		if c.texturas:
			pantalla.blit(bg, (0, 0))
			pantalla.blit(manzana, (c.manzana_x, c.manzana_y))
			
		else : 
			pantalla.fill(c.black)
			pg.draw.rect(pantalla, c.red, [c.manzana_x, c.manzana_y, 30, 30])


		


		snake_cabeza = [] # Lista con la posicion de la cabeza de la serpiente en el momento
		snake_cabeza.append(c.snake_x)
		snake_cabeza.append(c.snake_y)

		c.lista_snake.append(snake_cabeza)

		if len(c.lista_snake) > c.largo_snake:
			del c.lista_snake[0]
 
		for x in c.lista_snake[:-1]:
			if x == snake_cabeza:
				c.muerte = True
 
		snake(c.bloque_snake, c.lista_snake)

		if c.snake_y_cambio<0:
			pantalla.blit(snake_up, (c.snake_x, c.snake_y))
		if c.snake_y_cambio>0:
			pantalla.blit(snake_down, (c.snake_x, c.snake_y))
		if c.snake_x_cambio<0:
			pantalla.blit(snake_left, (c.snake_x, c.snake_y))
		if c.snake_x_cambio>0:
			pantalla.blit(snake_right,(c.snake_x,c.snake_y))

		if c.snake_x == c.manzana_x and c.snake_y == c.manzana_y:
			c.manzana_x = random.choice(c.x)
			c.manzana_y = random.choice(c.y)
			c.largo_snake += 1


		clock.tick(c.fps) # Fps
		pg.display.update() # Actualizamos la pantalla

	pg.quit()
	quit()

bucle_juego()










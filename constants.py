# Archivo donde se ubican las constantes. Nos permite un mayor flujo de trabajo al tener todas las constantes localizadas.

import random


###  Colores ###

blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
green_snake = (61,245,92)

###  Pantalla ## #

ancho       = 1280
alto        = 720




### Configuración ###

setup = True
fin         = False
muerte      = False
lista_snake =[]
largo_snake =1
fps = 20
texturas = True

### Posiciones ###

x = [] # Posibles posiciones en el eje x
for i in range(10, 1250, 30):
	x.append(i)

y = [] # Posibles posiciones en el eje y
for i in range(10, 700, 30):
	y.append(i)

snake_x        = x[21] # Escoge la posición x media al iniciar
snake_y        = y[12] # Escoge la posición y media al iniciar

snake_x_cambio = 0 # Cambio en las posiciones del jugador en el eje x
snake_y_cambio = 0 # Cambio en las posiciones del jugador en el eje y

manzana_x      = random.choice(x) # Escoge posicion aleatoria para la manzana en el eje x
manzana_y      = random.choice(y) # Escogeposicion aleatoria para la manzana en el eje y


bloque_snake = 30




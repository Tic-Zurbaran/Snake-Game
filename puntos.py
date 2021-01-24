import pygame
import numbers as np

class Game(object):

	def _init_(self, ancho juego, alto juego):
		pygame.display.set_caption("SnakeGame")
		self.ancho_juego = ancho_juego
		self.alto_juego = alto_juego
		self.display_juego 


	def display_ui(self, record):
		self.display_game.fill((255, 255, 255))
		score_txt = self.font.render("Score: ", True, (0, 0, 0))
		score_num = self.font.render(str(self.socre), True, (0, 0, 0))
		record_txt = self.font.render("Best: ", True, (0, 0, 0))
		record_txt = self.font.render(str(record), True, (0, 0, 0))

		pygame.draw.rect(self.display_game, (200, 200, 200), (0, self.stop_game, self.stop_game, 0))

#Esto hay que ajustarlo segun el tamaño de la ventana
											#|
											#|
										    #\/

		self.display_game.blit(score_txt, (45, 480))
		self.display_game.blit(score_num, (45, 480))
		self.display_game.blit(record_txt, (45, 480))
		self.display_game.blit(record_num, (45, 480))
		self.display_game.blit(self.fondo, (0, 0))

	def obtain_record(self, scor, record):
		return score if score >= record else record


def run():
	pygame.init()
	record = 0
	while True:
		game = Game("tamaño del juego")
		game.display_ui(record)

		pygame.display.update()


if __name__ == "__main__":
	run()
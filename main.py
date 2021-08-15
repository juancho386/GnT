import pygame
from pj import *

NEGRO  = (  0x00,   0,   0)
BLANCO = (0xff, 0xff, 0xff)
VERDE  = (0,   255,   0)
AZUL   = (0,     0,  255)
ROJO   = (255,   0,   0)


def main():
	BG_POS=0
	pygame.init()
	dimensiones = (800, 600)

	screen = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("G&T")
	background = pygame.image.load("./assets/backgrounds/bg0.png").convert()

	all_sprites = pygame.sprite.Group()
	player = Pj(screen)
	all_sprites.add(player)

	clock = pygame.time.Clock()
	quit = False
	while not quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					player.speed=-12
				if event.key == pygame.K_LEFT:
					player.speed=12
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					player.speed=0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.line(screen, VERDE, [0, 0], pygame.mouse.get_pos(), 5)



		# pygame.display.flip() # no se si va acá o abajo

		# Logic

		all_sprites.update()


		# Drawings
		BG_POS=BG_POS+player.speed
		screen.blit(background, [BG_POS,0])                 # fondo
		all_sprites.draw(screen)                            # personajes
		# draw_text(screen, str(score), 25, WIDTH // 2, 10) # textos
		# draw_shield_bar(screen, 5, 5, player.shield)      # HUD
		pygame.display.flip()                               # buffer dump
		clock.tick(18)                                      # TICK
	pygame.quit()

if __name__ == "__main__":
	main()

import pygame
import os

class Pj(pygame.sprite.Sprite):
	def __init__(self,sprites_location,screen):
		super().__init__()
		self.running_right = [] # cuadros de la animación de correr
		self.running_left = [] # cuadros de la animación de correr
		all_pj_sprite_images=os.listdir(sprites_location)
		all_pj_sprite_images.sort()
		for file in all_pj_sprite_images:
			if file.endswith(".png"):
				img=pygame.image.load(sprites_location+"/"+file).convert()
				img.set_colorkey((255,0,0xFC))
				self.running_right.append(img)
				self.running_left.append(
					pygame.transform.flip(img, True, False)
				)

		# estado inicial
		self.direction=">"
		self.running_state=0
		self.image = self.running_right[0]
		self.speed = 0

		self.rect = self.image.get_rect()
		self.rect.centerx = screen.get_width() // 2
		self.rect.bottom = screen.get_height() - 10
		self.framed_passed = 0

	def update(self):
		if self.speed==0:
			self.running_state=0
			self.framed_passed=0
		else:
			if self.framed_passed < 2: # cuantos frames banco antes de is al siguiente cuadro de running
				self.framed_passed+=1
			else:
				self.framed_passed=0
				if self.running_state==len(self.running_right)-1:
					self.running_state=1
				else:
					self.running_state+=1
		if self.direction=="<":
			self.image = self.running_left[self.running_state]
		if self.direction==">":
			self.image = self.running_right[self.running_state]

if __name__ == "__main__":
	main()

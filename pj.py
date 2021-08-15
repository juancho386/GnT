import pygame

class Pj(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.running_right = [] # cuadros de la animación de correr
		self.running_left = [] # cuadros de la animación de correr
		for i in range(4):
			img=pygame.image.load("assets/pj/p.{}.png".format(i)).convert()
			self.running_right.append(img)
			self.running_left.append(
				pygame.transform.flip(self.running_right[i], True, False)
			)

		self.direction=">"
		self.running_state=0
		self.image = self.running_right[self.running_state]
		self.image.set_colorkey((0,0,0))

		self.rect = self.image.get_rect()
		self.rect.x = 400 # screen.get_dimentions() // 2
		self.rect.y = 480 # screen.get_dimentions() - N
		self.framed_passed = 0
		self.speed = 0

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

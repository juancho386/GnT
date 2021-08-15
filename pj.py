import pygame

class Pj(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.running_images = []
		for i in range(3):
			self.running_images.append(pygame.image.load("assets/pj/p.{}.png".format(i)).convert())
		self.running_state=0
		self.image = self.running_images[self.running_state]
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 400 # screen.get_dimentions() // 2
		self.rect.y = 500 # screen.get_dimentions() - N
		self.framed_passed = 0
		self.delay = 5
		self.speed = 0

	def update(self):
		if self.speed==0:
			self.image = self.running_images[0]
			self.framed_passed=0
		else:
			if self.framed_passed < 5:
				self.framed_passed+=1
			else:
				self.framed_passed=0
				if self.running_state==len(self.running_images)-1:
					self.running_state=1
				else:
					self.running_state+=1
		self.image = self.running_images[self.running_state]

if __name__ == "__main__":
	main()

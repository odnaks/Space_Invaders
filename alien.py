import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""class for one of alien"""
	def __init__(self, ai_settings, screen):
		"""initialize alien and assignment his start position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		#self.image = pygame.image.load('image/star.bmp')
		self.image = pygame.image.load('image/mob1.bmp')
		self.rect = self.image.get_rect()
		#пришелец в левом верхнем углу экрана
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""display the alien in the current position"""
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""moving the alien to the right"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
	
	def	check_edges(self):
		"""if there is an alien on the edge, return TRUE"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	
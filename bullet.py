import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""The class to control the bullet, issued by the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Make a bullet object at the current ship position"""
		super(Bullet, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('image/bullet.bmp')
		self.rect = self.image.get_rect()
#		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	def update(self):
		"""Move the bullet up the screen"""
		self.y -= self.speed_factor
		self.rect.y = self.y
	def draw_bullet(self):
		"""Put a bullet on the screen"""
#		pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)

import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		"""initialize the attributes of the button"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		font_path = "slkscreb.ttf"
		self.font = pygame.font.SysFont(font_path, 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""convert the msg into a rectangle and align the text to the center"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

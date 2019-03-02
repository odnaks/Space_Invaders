import pygame
from pygame.sprite import Sprite

class Ship():
    def __init__(self, screen, ai_settings):
        """Init ship and define the start position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('image/ship0.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)
    def update(self):
        """update ship status with flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx

class Pers():
    def __init__(self, screen):
        """Init ship and define the start position"""
        self.screen = screen
        self.image = pygame.image.load('image/pers.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        """Draw ship in current position"""
        print ("yas")
        self.screen.blit(self.image, self.rect)
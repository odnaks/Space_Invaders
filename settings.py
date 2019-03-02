import pygame

class Settings():
    """Class for all settings out game"""
    def __init__(self):
        """Init STATIC settings game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_limit = 3
        self.bullets_allowed = 20
        #self.bullet_width = 300
        #self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.3
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """ Init DYNAMIC settings game """
        self.ship_speed_factor = 10        
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 20
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        """ increase the settings of speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

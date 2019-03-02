class GameStats():
	"""tracking statistics for the Alien Invasion game"""
	def __init__(self, ai_settings):
		"""initialize the statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		self.init_record()
	
	def reset_stats(self):
		"""initializes statistics changing during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
	
	def init_record(self):
		"""upload the high score"""
		filename = 'high_score'
		try:
			with open(filename) as file:
				self.high_score = int(file.read())
		except FileNotFoundError:
			with open(filename, 'w') as file:
				file.write(str(0))
				self.high_score = 0
class Location():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_position(self, x, y):
		self.x = x
		self.y = y

	def change_position(self, delta_x, delta_y):
		self.x += delta_x
		self.y += delta_y

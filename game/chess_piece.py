from game.Location import Location


class chess_piece():

	def __init__(self, x, y):
		self.name = "Default Piece"
		self.selected = False
		self.x = x
		self.y = y

	def __str__(self):
		return self.name

	def move_absolute(self, x, y):
		self.location.set_position(x, y)

	def move_relative(self, x, y):
		self.location.change_position(x, y)

	def highlight(self):
		pass

	def display(self, canvas):
		self.pos = canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="blue", outline="#DDD", width=4)

	def display_potential_moves(self):
		pass

	def get_potential_moves(self):
		return Location(1, 2)

	def check_if_can_move(self):
		pass

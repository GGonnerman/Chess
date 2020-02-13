from Window import Window
from game.Location import Location


class ChessPiece(object):

	def __init__(self, name, color, row, column, canvas, shade="#FFF"):
		self.name = name
		self.selected = False
		self.color = color
		self.row = row
		self.column = column
		self.shade = shade
		self.canvas = canvas

	def __str__(self):
		return self.name

	def move_absolute(self, row, column):
		self.location.set_position(row, column)

	def move_relative(self, row, column):
		self.location.change_position(row, column)

	def highlight(self):
		pass

	def display(self):
		print('displaying chess piece')
		box_length = Window.BOX_LENGTH
		diameter = 30
		self.canvas.create_centered_circle(self.row * box_length, self.column * box_length,
										   self.row * (box_length + 1), self.column * (box_length + 1),
										   diameter, fill="blue", outline="#DDD", width=4)

	def display_potential_moves(self):
		pass

	def get_potential_moves(self):
		return Location(1, 2)

	def check_if_can_move(self):
		pass

	def select(self):
		self.shade = "ABC"
		self.display()

	def deselect(self):
		self.shade = "FFF"
		self.display()

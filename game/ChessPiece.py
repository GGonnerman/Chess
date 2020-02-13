from game.Color import Color


class ChessPiece(object):

	def __init__(self, name, color, row, column, canvas, shade="#FFF"):
		self.name = name
		self.selected = False
		self.color = color
		self.row = row
		self.column = column
		self.shade = shade

	def __str__(self):
		return self.name

	def get_potential_moves(self, gameboard):
		potential_moves = []
		print('not epic')
		return potential_moves

	def check_if_can_move(self):
		pass

	def select(self):
		self.shade = "#333" if self.color == Color.BLACK else "#AAA"
		return {'fill': self.shade}

	def deselect(self):
		self.shade = self.color
		return {'fill': self.shade}

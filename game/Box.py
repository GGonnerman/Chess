from Window import Window
from game.Empty import Empty


class Box():

	def __init__(self, column, row, canvas, movement_hints):
		box_length = Window.BOX_LENGTH
		self.color = '#F7ECCA' if (row + column) % 2 == 0 else '#66442E'
		self.id = canvas.create_rectangle(row * box_length, column * box_length, (row + 1) * box_length,
										  (column + 1) * box_length, fill=self.color)
		self.piece = Empty(column, row, canvas)
		self.column = column
		self.row = row
		self.canvas = canvas
		self.movement_hints = movement_hints
		self.selected = False
		self.highlighted = False

	def delete_piece(self):
		self.piece = Empty(self.column, self.row, self.canvas)

	def set_piece(self, piece):
		self.piece = piece

	def get_piece(self):
		return self.piece

	def highlight(self):
		self.highlighted = True
		color = '#D7F7CA' if self.color == '#F7ECCA' else '#51662E'
		if self.movement_hints:
			return {'fill': color}
		else:
			return {'fill': self.color}

	def select(self):
		self.selected = True
		color = '#CAEDF7' if self.color == '#F7ECCA' else '#2E4866'
		return {'fill': color}

	def clear_coloring(self):
		self.selected = self.highlighted = False
		return {'fill': self.color}

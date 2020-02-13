from ChessPiece import ChessPiece
from Window import Window


class Pawn(ChessPiece):

	def __init__(self, color, row, column, canvas):
		super(Pawn, self).__init__("Pawn", color, row, column, canvas)

	def display(self):
		box_length = Window.BOX_LENGTH
		diameter = 30
		self.canvas.create_centered_circle(self.row * box_length, self.column * box_length,
										   (self.row + 1) * box_length, (self.column + 1) * box_length,
										   diameter, fill="#AAA", outline="#FFF", width=1)

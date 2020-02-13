from ChessPiece import ChessPiece
from game.Color import Color


class Empty(ChessPiece):

	def __init__(self, column, row, canvas):
		super(Empty, self).__init__("Empty", Color.WHITE, 0, 0, canvas)

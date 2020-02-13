from ChessPiece import ChessPiece
from Window import Window
from game.Color import Color
from game.Empty import Empty


class Pawn(ChessPiece):

	def __init__(self, color, row, column, canvas):
		super(Pawn, self).__init__("Pawn", color, row, column, canvas)
		box_length = Window.BOX_LENGTH
		diameter = 30
		self.id = canvas.create_centered_circle(self.column * box_length, self.row * box_length,
												(self.column + 1) * box_length, (self.row + 1) * box_length,
												diameter, fill=color, outline="black", width=1)
		print('iinited')

	def get_potential_moves(self, gameboard):
		potential_moves = [[-1, -1]]
		if (self.color == Color.BLACK):
			if isinstance(gameboard.piece_list[self.row + 1][self.column], Empty):
				potential_moves.append([self.row + 1, self.column])
		else:
			if isinstance(gameboard.piece_list[self.row - 1][self.column], Empty):
				potential_moves.append([self.row - 1, self.column])

		return potential_moves

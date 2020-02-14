from ChessPiece import ChessPiece
from game.Color import Color
from game.Empty import Empty
from game.SetMovement import SetMovement


class Pawn(ChessPiece, SetMovement):

	def __init__(self, color, row, column, canvas):
		super(Pawn, self).__init__("Pawn", color, row, column, canvas)

	def get_potential_moves(self, gameboard):
		potential_moves = []
		direction = 1 if self.color == Color.BLACK else -1
		potential_moves += self.check_movement_position(gameboard, [direction, 0])
		if (self.color == Color.BLACK and self.row == 1 or self.color == Color.WHITE and self.row == 6) and isinstance(
				gameboard.get_piece(self.row + direction, self.column), Empty):
			potential_moves += self.check_movement_position(gameboard, [2 * direction, 0])
		potential_moves += self.check_attacking_position(gameboard, [direction, -1], [direction, 1])
		return potential_moves

	def check_movement_position(self, gameboard, *changes):
		potential_moves = []
		for change in changes:
			row = self.row
			column = self.column
			row += change[0]
			column += change[1]
			if isinstance(gameboard.get_piece(row, column), Empty):
				potential_moves.append([row, column])
		return potential_moves

	def check_attacking_position(self, gameboard, *changes):
		potential_moves = []
		for change in changes:
			row = self.row
			column = self.column
			row += change[0]
			column += change[1]
			exists = gameboard.has_piece(row, column) and not isinstance(gameboard.get_piece(row, column), Empty)
			if exists and not gameboard.get_piece(row, column).color == self.color:
				potential_moves.append([row, column])
		return potential_moves

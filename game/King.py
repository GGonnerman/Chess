from game.ChessPiece import ChessPiece
from game.SetMovement import SetMovement


class King(ChessPiece, SetMovement):

	# TODO: Stale mate???
	# TODO: end game button?
	# TODO: restart button?
	def __init__(self, color, row, column, canvas):
		super(King, self).__init__("King", color, row, column, canvas)

	def get_potential_moves(self, gameboard):



		direction_list = [0, 1], [1, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]
		return self.check_position(gameboard, *direction_list)

		for row in range(len(gameboard.piece_list)):
			for column in range(len(gameboard.piece_list[0])):
				if isinstance(gameboard.get_piece(row, column), King) and gameboard.get_piece(row, column).color != self.color:
					king = gameboard.get_piece(row, column)

		delta_row = self.row - king.row
		delta_column = self.column - king.column

		print(f"MINE, row:{king.row}, column:{king.column}")
		print(f"KING, row:{self.row}, column:{self.column}")

		if delta_row > 2 and delta_column: return self.check_position(gameboard, *direction_list)

		return self.check_position(gameboard, *direction_list)

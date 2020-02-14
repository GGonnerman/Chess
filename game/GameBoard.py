from Color import Color
from TimeWidget import TimeWidget

from game.Bishop import Bishop
from game.Box import Box
from game.King import King
from game.Knight import Knight
from game.Pawn import Pawn
from game.Queen import Queen
from game.Rook import Rook


class GameBoard():

	def __init__(self, canvas, movement_hints=True):
		self.piece_list = [[Box(row, column, canvas, movement_hints) for column in range(8)] for row in range(8)]
		self.canvas = canvas
		self.selected = -1, -1
		self.movement_hints = movement_hints
		self.turn = Color.WHITE

	def __str__(self):
		output = ""
		for row in range(len(self.piece_list)):
			for column in range(len(self.piece_list)):
				output += self.piece_list[row][column].name
				if column == len(self.piece_list) - 1: break
				output += " "
			output += "\n" if row < len(self.piece_list) - 1 else ""
		return output

	def setup(self):

		for column in range(8):
			self.piece_list[1][column].set_piece(Pawn(Color.BLACK, 1, column, self.canvas))
			self.piece_list[6][column].set_piece(Pawn(Color.WHITE, 6, column, self.canvas))

		for column in [0, 7]:
			self.piece_list[0][column].set_piece(Rook(Color.BLACK, 0, column, self.canvas))
			self.piece_list[7][column].set_piece(Rook(Color.WHITE, 7, column, self.canvas))

		for column in [2, 5]:
			self.piece_list[0][column].set_piece(Bishop(Color.BLACK, 0, column, self.canvas))
			self.piece_list[7][column].set_piece(Bishop(Color.WHITE, 7, column, self.canvas))

		for column in [1, 6]:
			self.piece_list[0][column].set_piece(Knight(Color.BLACK, 0, column, self.canvas))
			self.piece_list[7][column].set_piece(Knight(Color.WHITE, 7, column, self.canvas))

		self.piece_list[0][3].set_piece(Queen(Color.BLACK, 0, 3, self.canvas))
		self.piece_list[7][3].set_piece(Queen(Color.WHITE, 7, 3, self.canvas))

		self.piece_list[0][4].set_piece(King(Color.BLACK, 0, 4, self.canvas))
		self.piece_list[7][4].set_piece(King(Color.WHITE, 7, 4, self.canvas))

	def flip_turn(self):
		self.turn = Color.WHITE if self.turn == Color.BLACK else Color.BLACK
		TimeWidget.flip_turn()

	def check_for_check(self):
		for row in range(len(self.piece_list)):
			for column in range(len(self.piece_list[0])):
				if isinstance(self.get_piece(row, column), King):
					if self.get_piece(row, column).color == Color.BLACK:
						black_king_position = [row, column]
					else:
						white_king_position = [row, column]
		print('Black king position:', black_king_position)
		print('White king position:', white_king_position)
		for row in range(len(self.piece_list)):
			for column in range(len(self.piece_list[0])):
				if self.get_piece(row, column).color == Color.BLACK:
					if black_king_position in self.get_piece(row, column).get_potential_moves(self):
						print('Black king in check')
				else:
					if white_king_position in self.get_piece(row, column).get_potential_moves(self):
						print('White king in check')

	def clear_selections(self):
		for row in range(len(self.piece_list)):
			for column in range(len(self.piece_list[0])):
				if self.piece_list[row][column].selected or self.piece_list[row][column].highlighted:
					self.deselect_piece(row, column)

	def click(self, row, column):
		if self.piece_list[row][column].highlighted:
			self.move_piece(self.get_piece(*self.selected), self.selected[0], self.selected[1], row, column)
			self.flip_turn()
			self.clear_selections()
			self.check_for_check()

		if self.get_piece(row, column).color == self.turn:
			self.clear_selections()
			self.select_piece(row, column)
			self.check_for_check()

	def select_piece(self, row, column):
		self.selected = row, column
		self.canvas.itemconfig(self.piece_list[row][column].id, self.piece_list[row][column].select())
		potential_moves = self.get_piece(row, column).get_potential_moves(self)
		for row, column in potential_moves:
			self.canvas.itemconfig(self.piece_list[row][column].id, self.piece_list[row][column].highlight())

	def deselect_piece(self, row, column):
		self.canvas.itemconfig(self.piece_list[row][column].id, self.piece_list[row][column].clear_coloring())

	def move_piece(self, game_piece, old_row, old_column, new_row, new_column):
		self.piece_list[new_row][new_column].set_piece(game_piece)
		self.piece_list[old_row][old_column].delete_piece()
		game_piece.row = new_row
		game_piece.column = new_column
		self.canvas.coords(game_piece.id, game_piece.get_coords())

	def has_piece(self, row, column):
		return row >= 0 and column >= 0 and row < len(self.piece_list) and column < len(self.piece_list[0])

	def get_piece(self, row, column):
		column = int(column)
		row = int(row)
		if not self.has_piece(row, column): return
		return self.piece_list[row][column].get_piece()

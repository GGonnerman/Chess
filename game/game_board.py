from game.Location import Location
from game.chess_piece import chess_piece


class game_board():

	def __init__(self):
		self.piece_list = [[None for i in range(8)] for j in range(8)]
		for column in range(8):
			for row in range(8):
				self.piece_list[column][row] = None

	def __str__(self):
		output = ""
		for i in range(len(self.piece_list)):
			for j in range(len(self.piece_list)):
				if (self.piece_list is chess_piece):
					output += self.piece_list[i][j].name
				else:
					output += "Empty"
				if j == len(self.piece_list) - 1:
					break
				output += " "
			output += "\n" if i < len(self.piece_list) - 1 else ""
		return output

	def setup(self):
		pass

	def click(self, x, y):
		self.select_piece(x, y)

	def drag(self):
		pass

	def select_piece(self, x, y):
		self.get_piece(x, y).highlight()

	def display(self, canvas):
		for column in self.piece_list:
			for item in column:
				if (item is chess_piece):
					item.display(canvas)

	def move_piece(self, old_x, old_y, new_x, new_y):

		if Location(1, 3) in self.piece_list[old_y][old_x].potential_moves():
			print("can be moved")

		self.piece_list[new_y][new_x] = self.piece_list[old_y][old_x]
		self.piece_list[old_y][old_x] = None
		return True

	def get_piece(self, x, y):
		return game_board[y][x]

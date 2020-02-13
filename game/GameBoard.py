from Color import Color
from Window import Window
from game.Empty import Empty
from game.Location import Location
from game.Pawn import Pawn


class GameBoard():

	def __init__(self, canvas):
		self.piece_list = [[Empty(column, row, canvas) for column in range(8)] for row in range(8)]
		self.canvas = canvas
		box_length = Window.BOX_LENGTH

		# Board drawing algorithm
		for i in range(8):
			for j in range(8):
				if (i + j) % 2 == 0:
					canvas.create_rectangle(i * box_length, j * box_length, i * box_length + box_length,
											j * box_length + box_length, fill='#F7ECCA')
				else:
					canvas.create_rectangle(i * box_length, j * box_length, i * box_length + box_length,
											j * box_length + box_length, fill='#66442E')

		self.setup()

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
			self.piece_list[1][column] = Pawn(Color.BLACK, 1, column, self.canvas)
			self.piece_list[6][column] = Pawn(Color.WHITE, 6, column, self.canvas)

		for column in [0, 7]:
			self.piece_list[0][column] = Pawn(Color.BLACK, 0, column, self.canvas)
			self.piece_list[7][column] = Pawn(Color.WHITE, 7, column, self.canvas)

	def click(self, row, column):
		for r in range(len(self.piece_list)):
			for c in range(len(self.piece_list[0])):
				if self.get_piece(r, c).shade != Color.WHITE and self.get_piece(r, c).shade != Color.BLACK:
					self.deselect_piece(r, c)
		if isinstance(self.piece_list[row][column], Empty):
			potential_moves = self.piece_list[row][column].get_potential_moves()
			print('potentials:' + ', '.join([str(x) for x in potential_moves]))
			print('we got ' + str(row) + ', ' + str(column))
			if (row, column) in potential_moves:
				print('gotem')
		else:
			self.select_piece(row, column)

	def select_piece(self, row, column):
		self.canvas.itemconfig(self.get_piece(row, column).id, self.get_piece(row, column).select())

	# for loc in self.get_piece(row, column).get_potential_moves():
	#	pass

	def deselect_piece(self, row, column):
		self.canvas.itemconfig(self.get_piece(row, column).id, self.get_piece(row, column).deselect())

	def move_piece(self, old_row, old_column, new_row, new_column):

		if Location(1, 3) in self.piece_list[old_row][old_column].potential_moves():
			print("can be moved")

		self.piece_list[new_row][new_column] = self.piece_list[old_column][old_row]
		self.piece_list[old_row][old_column] = Empty[old_column][old_row]
		return True

	def get_piece(self, row, column):
		column = int(column)
		row = int(row)
		return self.piece_list[row][column]

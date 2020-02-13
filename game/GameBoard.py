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
											j * box_length + box_length, fill='red')
				else:
					canvas.create_rectangle(i * box_length, j * box_length, i * box_length + box_length,
											j * box_length + box_length, fill='black')

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
			self.piece_list[1][column] = Pawn(Color.BLACK, 1, column, self.canvas, self)
			self.piece_list[6][column] = Pawn(Color.WHITE, 6, column, self.canvas, self)

		for column in [0, 7]:
			self.piece_list[0][column] = Pawn(Color.BLACK, 0, column, self.canvas, self)
			self.piece_list[7][column] = Pawn(Color.WHITE, 7, column, self.canvas, self)

	def click(self, row, column):
		self.select_piece(row, column)

	def drag(self):
		pass

	def select_piece(self, row, column):
		self.get_piece(row, column).select()
		self.get_piece(row, column).display()

	def display(self):
		for column in self.piece_list:
			for item in column:
				item.display()

	def move_piece(self, old_row, old_column, new_row, new_column, ):

		if Location(1, 3) in self.piece_list[old_row][old_column].potential_moves():
			print("can be moved")

		self.piece_list[new_row][new_column] = self.piece_list[old_column][old_row]
		self.piece_list[old_row][old_column] = Empty[old_column][old_row]
		return True

	def get_piece(self, row, column):
		column = int(column)
		row = int(row)
		print("got row:", row, "col:", column)
		return self.piece_list[row][column]

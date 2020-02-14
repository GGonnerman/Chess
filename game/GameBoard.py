from Color import Color
from Window import Window
from game.Empty import Empty
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
			print(self.selected[0])
			potential_moves = self.get_piece(*self.selected).get_potential_moves(self)
			print('potentials:' + ', '.join([str(x) for x in potential_moves]))
			if [row, column] in potential_moves:
				print('we gotem')
				print('type ' + str(type(self.get_piece(*self.selected))))
				print('id ' + str(self.get_piece(*self.selected).id))
				self.move_piece(self.get_piece(*self.selected), self.selected[0], self.selected[1], row, column)
		else:
			self.select_piece(row, column)

	def select_piece(self, row, column):
		self.selected = row, column
		self.canvas.itemconfig(self.get_piece(row, column).id, self.get_piece(row, column).select())

	# for loc in self.get_piece(row, column).get_potential_moves():
	#	pass

	def deselect_piece(self, row, column):
		self.canvas.itemconfig(self.get_piece(row, column).id, self.get_piece(row, column).deselect())

	def move_piece(self, game_piece, old_row, old_column, new_row, new_column):
		self.piece_list[new_row][new_column] = game_piece
		self.piece_list[old_row][old_column] = Empty(old_row, old_column, self.canvas)
		game_piece.row = new_row
		game_piece.column = new_column
		self.canvas.move(game_piece.id, new_row, new_column)
		print('moved')

	def get_piece(self, row, column):
		column = int(column)
		row = int(row)
		return self.piece_list[row][column]

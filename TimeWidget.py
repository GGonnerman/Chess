import Tkinter

from game.Color import Color


class TimeWidget():
	turn = Color.WHITE

	def __init__(self, root, canvas):
		self.id = Tkinter.Text(height=2, width=17)
		self.id.grid(row=0, column=1)
		self.canvas = canvas
		self.white_time = [0, 0, 0]
		self.black_time = [0, 0, 0]
		self.update_white()

	@staticmethod
	def flip_turn():
		TimeWidget.turn = Color.WHITE if TimeWidget.turn == Color.BLACK else Color.BLACK

	def update_white(self):
		self.white_time[2] += 1
		self.white_time[1] = (int)(self.white_time[2] / 10)
		if self.white_time[1] >= 60:
			self.white_time[2] = 0
			self.white_time[1] = 0
			self.white_time[0] += 1
		self.display()
		if TimeWidget.turn == Color.WHITE:
			self.canvas.after(100, self.update_white)
		else:
			self.canvas.after(100, self.update_black)

	def update_black(self):
		self.black_time[2] += 1
		self.black_time[1] = (int)(self.black_time[2] / 10)
		if self.black_time[1] >= 60:
			self.black_time[2] = 0
			self.black_time[1] = 0
			self.black_time[0] += 1
		self.display()
		if TimeWidget.turn == Color.WHITE:
			self.canvas.after(100, self.update_white)
		else:
			self.canvas.after(100, self.update_black)

	def display(self):
		self.id.delete("1.0", Tkinter.END)
		self.id.insert(Tkinter.END, 'Black time: %02d:%02d\nWhite time: %02d:%02d' % (
		self.black_time[0], self.black_time[1], self.white_time[0], self.white_time[1]))

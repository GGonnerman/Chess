from Tkinter import *

from CanvasImpl import CanvasImpl


class Window():
	SIDE_LENGTH = 400
	BOX_LENGTH = SIDE_LENGTH / 8

	def __init__(self):
		self.root = Tk();
		self.canvas = CanvasImpl(self.root, width=Window.SIDE_LENGTH, height=Window.SIDE_LENGTH, background='#AAAAAA')
		self.canvas.grid(row=0, rowspan=2, column=1)

	def get_root(self):
		return self.root

	def get_canvas(self):
		return self.canvas

	def bind_click(self, click_event):
		self.canvas.focus_set()
		self.canvas.bind("<Button-1>", click_event)

	def bind_release(self, release_event):
		self.canvas.focus_set()
		self.canvas.bind("<ButtonRelease-1>", release_event)

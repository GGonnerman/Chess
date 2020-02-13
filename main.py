from __future__ import print_function

from Tkinter import *

from game.game_board import game_board

#####
# Create root window
#####

root = Tk();

x = 0
y = 0
r = 0


######
# Create Controller
#######
def click_event(event):
	canvas.focus_set()
	print("x:" + str(event.x) + ", y:" + str(event.y))


def release_event(event):
	canvas.focus()
	print("x:" + str(event.x) + ", y:" + str(event.y))


def process_click_event(x, y):
	x /= 8
	y /= 8
	game_board.click(x, y)


######
# Create View
#######
# Create and place a canvas
canvas = Canvas(root, width=300, height=300, background='#AAAAAA')
canvas.grid(row=0, rowspan=2, column=1)
canvas.bind("<Button-1>", click_event)
canvas.bind("<ButtonRelease-1>", release_event)
gb = game_board()
gb.display(canvas)
print(gb)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x - r, y - r, x + r, y + r, outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()

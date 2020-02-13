from math import floor

from Window import Window
from game.GameBoard import GameBoard

#####
# Create root window
#####

window = Window()

######
# Create Controller
#######

game_board = GameBoard(window.get_canvas())
game_board.setup()
game_board.display()

window.get_canvas().create_centered_circle(0, 0, 150, 150, 100)


def click_event(event):
	column = floor(event.x / Window.BOX_LENGTH)
	row = floor(event.y / Window.BOX_LENGTH)
	game_board.click(row, column)
	game_board.display()
	print("row:", row, "col:", column)
	print("Clicked on " + game_board.get_piece(row, column).name)


def release_event(event):
	print("x:" + str(event.x) + ", y:" + str(event.y))


window.bind_click(click_event)


######
# Create View
#######
# Create and place a canvas

#######
# Event Loop
#######
root = window.get_root()
root.mainloop()

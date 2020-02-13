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

def process_click(event):
	row = int(event.y / Window.BOX_LENGTH)
	column = int(event.x / Window.BOX_LENGTH)
	return row, column


def click_event(event):
	row, column = process_click(event)
	game_board.click(row, column)
	print("Row: " + str(row) + " Column: " + str(column))
	print("Clicked on " + game_board.get_piece(row, column).name)


def release_event(event):
	row, column = process_click(event)


window.bind_click(click_event)
window.bind_release(release_event)

######
# Create View
#######
# Create and place a canvas

#######
# Event Loop
#######
root = window.get_root()
root.mainloop()

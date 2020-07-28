# constant - value once created can't be changed

class Config():
	Fps = 9
	menu_Fps = 60
	window_Height = 480
	window_Width = 640
	CellSize = 20

	assert window_Width % CellSize == 0, "Window width must be a multiple of Cell size."
	assert window_Height % CellSize == 0, "Window height must be a multiple of Cell size."

	# determine how far apart to draw line to determine the cells
	# alse helps how big the apple and the snake cell will be
	cellWidth = int(window_Width/CellSize)
	cellHeight = int(window_Height/CellSize)

	# Colors
	White = (255,255,255)
	Black = (0,0,0)
	Red = (255,0,0)
	Green = (0,255,0)
	DarkGreen = (0,155,0)
	DarkGray = (40,40,40)
	BG_Color = Black
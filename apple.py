# class takes all these different data types 
# function you can call and it does stuff for you
import random
from config import Config

class Apple():
	def __init__(self):
		self.setLocation()

	# any where on the game board starting from the far left corner
	def setLocation(self):
		# we have so many cells in a game, so 
		# give us a number from 0 all the way to the end 
		# minus one 
		# any where from the start on the left to the right
		# - 1 because in programming between 0 and number
		# if you say the width is 16 in terms of the actual value
		# it goes from 0 - 15: just cell width it might pick
		# number 16 instead of 15.
		self.x = random.randint(0, Config.cellWidth - 1)
		self.y = random.randint(0, Config.cellHeight - 1)

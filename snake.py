from config import Config
import random

class Snake():
	Up = 'up'
	Down = 'down'
	Left = 'left'
	Right = 'right'
	Head = 0

	def __init__(self):
		self.x = random.randint(5, Config.cellWidth - 6)
		self.y = random.randint(5, Config.cellHeight - 6)
		self.direction = self.Right
		self.snakeCoords = [{'x': self.x, 'y':self.y},
							{'x':self.x-1, 'y':self.y},
							{'x':self.x - 2, 'y':self.y}]
	def update(self, apple):
		if self.wormCoords[self.Head]['x'] == apple.x and self.wormCoords[self.Head]['y'] == apple.y:
			apple.setLocation()
		else:
			del self.wormCoords[-1]

		if self.direction == self.Up:
			newHead = {'x': self.wormCoords[self.Head]['x'],
					'y': self.wormCoords[self.Head]['y'] - 1}
		elif self.direction == self.Down:
			newHead = {'x': self.wormCoords[self.Head]['x'],
						'y': self.wormCoords[self.Head]['y']+1}
		elif self.direction == self.Left:
			newHead = {'x': self.wormCoords[self.Head]['x'] -1, 
						'y': self.wormCoords[self.Head]['y']}
		elif self.direction == self.Right:
			newHead = {'x': self.wormCoords[self.Head]['x'] + 1,
						'y': self.wormCoords[self.Head]['y']}
		self.wormCoords.insert(0, newHead)

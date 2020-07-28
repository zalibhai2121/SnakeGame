from config import Config
from snake import Snake
from apple import Apple
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

class Game():

	# this function gets run automarically
	# constructor -- initialization
	# anything you want gets initialized theres
	def __init__(self):
		# starts the game
		pygame.init()

		# window 
		self.screen = pygame.display.set_model((Config.window_Width, Config.window_Height))
		# clock cycle
		self.clock = pygame.time.Clock()
		self.basicFont = pygame.font.Font('freesansbold.ttf', 18)
		# title bar
		pygame.display.set_caption('Snake Game')
		self.apple = Apple()
		self.snake = Snake()

	def draw(self):
		self.screen.fill(Config.BG_Color)
		# draw snake grid, apple, score
		self.drawGrid()
		self.drawSnake()
		self.Score(len(self.snake.wormCoords) - 3)
		self.drawApple()
		pygame.display.update()
		self.clock.tick(Config.Fps)

	def handleKeyEvents(self, event):
		if event.key == pygame.K_LEFT or event.key == pygame.K_a and self.snake.direction != self.snake.Right:
			self.snake.direction = self.snake.Left
		elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and self.snake.direction != self.snake.Left:
			self.snake.direction = self.snake.Right
		elif event.key == pygame.K_UP or event.key == pygame.K_w and self.snake.direction != self.snake.Down:
			self.snake.direction = self.snake.Up
		elif event.key == pygame.K_DOWN or event.key == pygame.K_s and self.snake.direction != self.snake.Up:
			self.snake.direction = self.snake.Down
		elif event.key == pygame.K_ESCAPE:
			pygame.quit()

	def drawGrid(self):
		for x in range(0, Config.window_Width, Config.CellSize):
			pygame.draw.line(self.screen, Config.White, (x, 0), (Config.window_Width,y))
		for y in range(0, Config.window_Height, Config.CellSize):
			pygame.draw.line(self.screen, Config.White, (0,y), (Config.window_Width,y))

	def drawSnake(self):
		for coord in self.snake.wormCoords:
			x = coord['x'] * Config.CellSize
			y = coord['y'] * Config.CellSize
			snakeSegRect = pygame.Rect(x, y, Config.CellSize)
			pygame.draw.rect(self.screen, Config.DarkGreen, snakeSegRect)
			snakeInnerRect = pygame.Rect(x+4,y+4, Config.CellSize-8, Config.CellSize-8)
			pygame.draw.rect(self.screen, Config.Green, snakeInnerRect)

	def drawApple(self):
		x = self.apple.x * Config.CellSize
		y = self.apple.y * Config.CellSize
		appleRect = pygame.Rect(x, y, Config.CellSize)
		pygame.draw.rect(self.screen, Config.Red, appleRect)

	def Score(self):
		scoreSurf = self.basicFont.render('Score: %s' % (score), True, Config.White)
		scoreRect = scoreSurf.get_rect()
		scoreRect.topleft = (Config.window_Width -120, 10)
		self.screen.blit(scoreSurf, scoreRect)

	def KeyPress(self):
		if len(pygame.event.get(pygame.QUIT)) > 0:
			pygame.quit()

		keyUp = pygame.event.get(pygame.KEYUP)

		if len(keyUp) == 0:
			return None

		if keyUp[0].key == pygame.K_ESCAPE:
			pygame.quit()
			quit()

		return keyUp[0].key

	def Reset(self):
		del self.snake
		del self.apple
		self.snake = Snake()
		self.apple = Apple()

		return True

	def KeyMsg(self):
		pressKeySurf = self.basicFont.render('Press a key to play.', True, Config.DarkGray)
		pressKeyRect = pressKeySurf.get_rect()
		pressKeyRect.topleft = (Config.window_Width -200, Config.window_Height -30)
		self.screen.blit(pressKeySurf, pressKeyRect)

	def GameOver(self):
		if (self.snake.wormCoords[self.snake.Head]['x'] == -1 or
			self.snake.wormCoords[self.snake.Head]['x'] == Config.cellWidth or
			self.snake.wormCoords[self.snake.Head]['y'] == -1 or 
			self.snake.wormCoords[self.snake.Head]['y'] == Config.cellHeight):
			return self.Reset()
		for snakeBody in self.snake.wormCoords[1:]:
			if snakeBody['x'] == self.snake.wormCoords[self.snake.Head]['x'] and snakeBody['y']== self.snake.wormCoords[self.snake.Head]['y']:
				return self.Reset()

	def DisplayGameOver(self):
		gameoverFont = pygame.font.Font('freesansbold.ttf', 150)
		gameSurf = gameoverFont.render('Game', True, Config.White)
		overSurf = gameoverFont.render('Over', True, Config.White)
		gameRect = gameSurf.get_rect()
		overRect = overSurf.get_rect()
		gameRect.midtop = (Config.window_Width/2, 10)
		overRect.midtop = (Config.window_Width/2, gameRect.height +10+25)
		self.screen.blit(gameSurf, gameRect)
		self.screen.blit(overSurf, overRect)

		self.KeyMsg()
		pygame.display.update()
		pygame.time.wait(500)

		self.KeyPress()

		while True:
			if self.KeyPress():
				pygame.event.get()
				return

	def startSceen(self):
		titleFont = pygame.font.Font('freesansbold.ttf', 100)
		titleSurf1 = titleFont.render('SnakeGame', True, Config.White)

	def run(self):
		self.startSceen()
		
		while True:
			self.gameLoop()
			self.DisplayGameOver()

	def gameLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self.handleKeyEvents(event)
			
			snake.update(self.apple)
			self.draw
			if self.isGameOver():
				break




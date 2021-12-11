import pygame

pygame.init()

pygame.font.init()

import random
import time
import json

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Tetris Demake')

from startGrid import * 

with open('player_save.json') as file:
	playerData = json.load(file)

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

textblack = black

Iblue = (0, 209, 255)
Lorange = (255, 131, 0)
Jblue = (0, 109, 255)
Tpurple = (227, 45, 255)
Zred = (255, 56, 69)
Sgreen = (33, 255, 51)
Oyellow = (255, 250, 0)

bgRed = 255
bgGreen = 255
bgBlue = 255

blockfade = 0

clock = pygame.time.Clock()
frame = 0

class Block:
	def __init__(self, x, y, pieceNum, idnumber, anchor):
		self.x = x
		self.y = y
		self.piece = pieceNum
		self.id = idnumber
		self.anchor = anchor
	def update(self):
		if self.y >= 0:
			grid[self.y][self.x] = self.piece

blocklist = []

class Piece:
	def __init__(self, pieceNum, idnumber, next=3):
		self.piece = pieceNum
		self.id = idnumber
		if next == 0:
			self.falling = True
		else:
			self.falling = False
		self.next = next
		self.held = False
		self.fallen = False
		if self.piece == 1:
			self.blockformation = [0, "110011"]
			self.color = Zred
		elif self.piece == 2:
			self.blockformation = [0, "001111"]
			self.color = Lorange
		elif self.piece == 3:
			self.blockformation = [1, "1111"]
			self.color = Oyellow
		elif self.piece == 4:
			self.blockformation = [0, "011110"]
			self.color = Sgreen
		elif self.piece == 5:
			self.blockformation = [2, "1111"]
			self.color = Iblue
		elif self.piece == 6:
			self.blockformation = [0, "100111"]
			self.color = Jblue
		else:
			self.blockformation = [0, "010111"]
			self.color = Tpurple
	def startFall(self):
		if self.piece == 1:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, True))
			blocklist.append(Block(5, -1, self.piece, self.id, False))
			blocklist.append(Block(5, -2, self.piece, self.id, False))
		elif self.piece == 2:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(5, 0, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, True))
			blocklist.append(Block(4, -2, self.piece, self.id, False))
		elif self.piece == 3:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(5, 0, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, False))
			blocklist.append(Block(5, -1, self.piece, self.id, False))
		elif self.piece == 4:
			blocklist.append(Block(5, 0, self.piece, self.id, False))
			blocklist.append(Block(5, -1, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, True))
			blocklist.append(Block(4, -2, self.piece, self.id, False))
		elif self.piece == 5:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, True))
			blocklist.append(Block(4, -2, self.piece, self.id, False))
			blocklist.append(Block(4, -3, self.piece, self.id, False))
		elif self.piece == 6:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(5, 0, self.piece, self.id, False))
			blocklist.append(Block(5, -1, self.piece, self.id, True))
			blocklist.append(Block(5, -2, self.piece, self.id, False))
		elif self.piece == 7:
			blocklist.append(Block(4, 0, self.piece, self.id, False))
			blocklist.append(Block(4, -1, self.piece, self.id, True))
			blocklist.append(Block(5, -1, self.piece, self.id, False))
			blocklist.append(Block(4, -2, self.piece, self.id, False))
	def renderNext(self):
		if self.next == 3:
			if self.blockformation[0] == 0:
				for x in range(6):
					if self.blockformation[1][x] == "1":
						if x <= 2:
							borderRect(self.color, black, center(24, 40, 515) + 8 * x, center(16, 40, 190), 8, 8, 1)
						else:
							borderRect(self.color, black, center(24, 40, 515) + 8 * (x - 3), center(16, 40, 190) + 8, 8, 8, 1)
			if self.blockformation[0] == 1:
				for x in range(4):
					if x <= 1:
						borderRect(self.color, black, center(16, 40, 515) + 8 * x, center(16, 40, 190), 8, 8, 1)
					else:
						borderRect(self.color, black, center(16, 40, 515) + 8 * (x - 2), center(16, 40, 190) + 8, 8, 8, 1)
			if self.blockformation[0] == 2:
				for x in range(4):
					borderRect(self.color, black, center(32, 40, 515) + 8 * x, center(8, 40, 190), 8, 8, 1)
		if self.next == 2:
			if self.blockformation[0] == 0:
				for x in range(6):
					if self.blockformation[1][x] == "1":
						if x <= 2:
							borderRect(self.color, black, center(33, 55, 515) + 11 * x, center(22, 55, 125), 11, 11, 1)
						else:
							borderRect(self.color, black, center(33, 55, 515) + 11 * (x - 3), center(22, 55, 125) + 11, 11, 11, 1)
			if self.blockformation[0] == 1:
				for x in range(4):
					if x <= 1:
						borderRect(self.color, black, center(22, 55, 515) + 11 * x, center(22, 55, 125), 11, 11, 1)
					else:
						borderRect(self.color, black, center(22, 55, 515) + 11 * (x - 2), center(22, 55, 125) + 11, 11, 11, 1)
			if self.blockformation[0] == 2:
				for x in range(4):
					borderRect(self.color, black, center(44, 55, 515) + 11 * x, center(11, 55, 125), 11, 11, 1)
		if self.next == 1:
			if self.blockformation[0] == 0:
				for x in range(6):
					if self.blockformation[1][x] == "1":
						if x <= 2:
							borderRect(self.color, black, center(42, 70, 515) + 14 * x, center(28, 70, 45), 14, 14, 1)
						else:
							borderRect(self.color, black, center(42, 70, 515) + 14 * (x - 3), center(28, 70, 45) + 14, 14, 14, 1)
			if self.blockformation[0] == 1:
				for x in range(4):
					if x <= 1:
						borderRect(self.color, black, center(28, 70, 515) + 14 * x, center(28, 70, 45), 14, 14, 1)
					else:
						borderRect(self.color, black, center(28, 70, 515) + 14 * (x - 2), center(28, 70, 45) + 14, 14, 14, 1)
			if self.blockformation[0] == 2:
				for x in range(4):
					borderRect(self.color, black, center(56, 70, 515) + 14 * x, center(14, 70, 45), 14, 14, 1)
	def renderHeld(self):
		if self.blockformation[0] == 0:
			for x in range(6):
				if self.blockformation[1][x] == "1":
					if x <= 2:
						borderRect(self.color, black, center(42, 70, 165) + 14 * x, center(28, 70, 45), 14, 14, 1)
					else:
						borderRect(self.color, black, center(42, 70, 165) + 14 * (x - 3), center(28, 70, 45) + 14, 14, 14, 1)
		if self.blockformation[0] == 1:
			for x in range(4):
				if x <= 1:
					borderRect(self.color, black, center(28, 70, 165) + 14 * x, center(28, 70, 45), 14, 14, 1)
				else:
					borderRect(self.color, black, center(28, 70, 165) + 14 * (x - 2), center(28, 70, 45) + 14, 14, 14, 1)
		if self.blockformation[0] == 2:
			for x in range(4):
				borderRect(self.color, black, center(56, 70, 165) + 14 * x, center(14, 70, 45), 14, 14, 1)
	def update(self):
		if self.falling == True:
			for block in blocklist:
				if block.id == self.id:
					block.y += 1

def calculateFade(color):
	return color[0] / 51, color[1] / 51, color[2] / 51

def subtractFade(color, fade):
	tempcolor = [color[0], color[1], color[2]]
	tempcolor[0] -= fade[0]
	tempcolor[1] -= fade[1]
	tempcolor[2] -= fade[2]
	return tempcolor[0], tempcolor[1], tempcolor[2]

def borderRect(color, bordercolor, x, y, w, h, borderwidth):
	pygame.draw.rect(window, color, (x, y, w, h))
	pygame.draw.rect(window, bordercolor, (x, y, w, h), borderwidth)

# Capital W is width, capital H is height
def centerText(object, screen, addition):
	return ((screen - object.get_size()[0]) / 2) + addition

def center(object, screen, addition):
	return ((screen - object) / 2) + addition

largeFont = pygame.font.SysFont('Arial', 36)
midFont = pygame.font.SysFont('Arial', 24)
smallFont = pygame.font.SysFont('Arial', 20)

pieces = []
piecenumber = 0
for x in range(0, 4):
	piecenumber = x
	pieces.append(Piece(random.randint(1, 7), piecenumber, piecenumber))
pieces[0].startFall()

game = 'playing'

fallspeed = 60
originalfallspeed = 60

RedFade = calculateFade(Zred)
OrangeFade = calculateFade(Lorange)
YellowFade = calculateFade(Oyellow)
GreenFade = calculateFade(Sgreen)
CyanFade = calculateFade(Iblue)
BlueFade = calculateFade(Jblue)
PurpleFade = calculateFade(Tpurple)

score = 0
holdcooldown = False
endloop = 0
timesheld = 0

pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play(-1)

gameLoop = True
while gameLoop:
	window.fill((bgRed, bgGreen, bgBlue))

	colors = [Zred, Lorange, Oyellow, Sgreen, Iblue, Jblue, Tpurple]

	keys = pygame.key.get_pressed()

	fallspeed = originalfallspeed
	if keys[pygame.K_DOWN]:
		fallspeed = 4

	startfall = False
	collideBlock = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameLoop = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and game == 'playing':
				for piece in pieces:
					if piece.falling == True:
						farleftx = 10
						inblock = False
						for block in blocklist:
							if block.x < farleftx and block.id == piece.id:
								farleftx = block.x
						if farleftx > 0:
							for block in blocklist:
								if block.id == piece.id:
									block.x -= 1
						for block in blocklist:
							if block.id == piece.id:
								for subblock in blocklist:
									if subblock.x == block.x and subblock.y == block.y and subblock.id != block.id:
										inblock = True
						if inblock == True:
							for block in blocklist:
								if block.id == piece.id:
									block.x += 1
			if event.key == pygame.K_RIGHT and game == 'playing':
				for piece in pieces:
					if piece.falling == True:
						farrightx = 0
						inblock = False
						for block in blocklist:
							if block.x > farrightx and block.id == piece.id:
								farrightx = block.x
						if farrightx < 9:
							for block in blocklist:
								if block.id == piece.id:
									block.x += 1
						for block in blocklist:
							if block.id == piece.id:
								for subblock in blocklist:
									if subblock.x == block.x and subblock.y == block.y and subblock.id != block.id:
										inblock = True
						if inblock == True:
							for block in blocklist:
								if block.id == piece.id:
									block.x -= 1
			if event.key == pygame.K_UP and game == 'playing':
				for piece in pieces:
					if piece.falling == True:
						while not(collideBlock):
							for block in blocklist:
								if block.id == piece.id:
									block.y += 1
							score += 2
							for block in blocklist:
								if block.id == piece.id:
									for subblock in blocklist:
										if (subblock.x == block.x and subblock.y == block.y and subblock.id != block.id) or block.y > 19:
											collideBlock = True
						for block in blocklist:
							if block.id == piece.id:
								block.y -= 1
						score -= 2
						piece.update()
			if event.key == pygame.K_b and game == 'playing' and holdcooldown == False:
				removelist = []
				for piece in pieces:
					if piece.falling == True:
						for block in blocklist:
							if piece.id == block.id:
								removelist.append(block)
						for block in removelist:
							blocklist.remove(block)
						timesheld += 1
						piece.held = True
						piece.falling = False
						if timesheld == 1:
							for subpiece in pieces:
								if subpiece.next > 0:
									subpiece.next -= 1
							piecenumber += 1
							pieces.append(Piece(random.randint(1, 7), piecenumber)) 
						startfall = True
						holdcooldown = True
					if piece.held == True and holdcooldown == False:
						piece.held = False
						piece.startFall()
						piece.falling = True
			if event.key == pygame.K_SPACE and game == 'playing':
				for piece in pieces:
					if piece.falling == True:
						if piece.piece == 1 or piece.piece == 2 or piece.piece == 4 or piece.piece == 6 or piece.piece == 7:
							for block in blocklist:
								if block.id == piece.id and block.anchor == True:
									anchorx = block.x
									anchory = block.y
							canspin = True
							for block in blocklist:
								if block.id == piece.id and block.anchor == False:
									if block.y > anchory and block.x == anchorx:
										distance = abs(block.y - anchory)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx - distance and subblock.y == anchory:
												canspin = False 
										#block.y = anchory
										#block.x = anchorx - distance
									elif block.y < anchory and block.x == anchorx:
										distance = abs(block.y - anchory)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx + distance and subblock.y == anchory:
												canspin = False 
										#block.y = anchory
										#block.x = anchorx + distance
									elif block.x < anchorx and block.y == anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx and subblock.y == anchory - distance:
												canspin = False 
										#block.x = anchorx
										#block.y = anchory - distance
									elif block.x > anchorx and block.y == anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx and subblock.y == anchory + distance:
												canspin = False
										#block.x = anchorx
										#block.y = anchory + distance 
									elif block.x > anchorx and block.y > anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx - distance and subblock.y == block.y:
												canspin = False
										#block.x = anchorx - distance
									elif block.x < anchorx and block.y > anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == block.x and subblock.y == anchory - distance:
												canspin = False
										#block.y = anchory - distance
									elif block.x < anchorx and block.y < anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx + distance and subblock.y == block.y:
												canspin = False
										#block.x = anchorx + distance
									elif block.x > anchorx and block.y < anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == block.x and subblock.y == anchory + distance:
												canspin = False
										#block.y = anchory + distance
							if canspin == True:
								for block in blocklist:
									if block.id == piece.id and block.anchor == False:
										if block.y > anchory and block.x == anchorx:
											distance = abs(block.y - anchory) 
											block.y = anchory
											block.x = anchorx - distance
										elif block.y < anchory and block.x == anchorx:
											distance = abs(block.y - anchory)
											block.y = anchory
											block.x = anchorx + distance
										elif block.x < anchorx and block.y == anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx
											block.y = anchory - distance
										elif block.x > anchorx and block.y == anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx
											block.y = anchory + distance 
										elif block.x > anchorx and block.y > anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx - distance
										elif block.x < anchorx and block.y > anchory:
											distance = abs(block.x - anchorx)
											block.y = anchory - distance
										elif block.x < anchorx and block.y < anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx + distance
										elif block.x > anchorx and block.y < anchory:
											distance = abs(block.x - anchorx)
											block.y = anchory + distance
						elif piece.piece == 5:
							for block in blocklist:
								if block.id == piece.id and block.anchor == True:
									anchorx = block.x
									anchory = block.y
							canspin = True
							for block in blocklist:
								if block.id == piece.id and block.anchor == False:
									if block.y > anchory and block.x == anchorx:
										distance = abs(block.y - anchory) 
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx - distance and subblock.y == anchory:
												canspin = False
										#block.y = anchory
										#block.x = anchorx - distance
									elif block.y < anchory and block.x == anchorx:
										distance = abs(block.y - anchory)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx + distance and subblock.y == anchory:
												canspin = False
										#block.y = anchory
										#block.x = anchorx + distance
									elif block.x < anchorx and block.y == anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx and subblock.y == anchory + distance:
												canspin = False
										#block.x = anchorx
										#block.y = anchory + distance
									elif block.x > anchorx and block.y == anchory:
										distance = abs(block.x - anchorx)
										for subblock in blocklist:
											if subblock.id != piece.id and subblock.x == anchorx and subblock.y == anchory - distance:
												canspin = False
										#block.x = anchorx
										#block.y = anchory - distance
							if canspin == True:
								for block in blocklist:
									if block.id == piece.id and block.anchor == False:
										if block.y > anchory and block.x == anchorx:
											distance = abs(block.y - anchory) 
											block.y = anchory
											block.x = anchorx - distance
										elif block.y < anchory and block.x == anchorx:
											distance = abs(block.y - anchory)
											block.y = anchory
											block.x = anchorx + distance
										elif block.x < anchorx and block.y == anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx
											block.y = anchory + distance
										elif block.x > anchorx and block.y == anchory:
											distance = abs(block.x - anchorx)
											block.x = anchorx
											block.y = anchory - distance 
			if event.key == pygame.K_p:
				if game == 'playing':
					game = 'pause'
					pygame.mixer.music.set_volume(0.1)
					bgRed, bgBlue, bgGreen = 225, 225, 225
					gray = (175, 175, 175)
				elif game == 'pause':
					game = 'playing'
					pygame.mixer.music.set_volume(1.0)
					bgRed, bgBlue, bgGreen = 255, 255, 255
					gray = (200, 200, 200)
			if event.key == pygame.K_m:
				playerData["music_on"] = not playerData["music_on"]
				if playerData["music_on"]:
					pygame.mixer.music.set_volume(1.0)
				with open('player_save.json', 'w') as file:
					json.dump(playerData, file, indent=4)

	if playerData["music_on"] == False:
		pygame.mixer.music.set_volume(0)

	piecefallen = False
	for piece in pieces:
		if piece.falling == True:
			farleftx = 9
			farrightx = 0
			for block in blocklist:
				if block.id == piece.id:
					if block.x < farleftx:
						farleftx = block.x
					if block.x > farrightx:
						farrightx = block.x
			if farleftx < 0:
				distance = abs(0 - farleftx)
				for block in blocklist:
					if block.id == piece.id:
						block.x += distance
			if farrightx > 9:
				distance = abs(9 - farrightx)
				for block in blocklist:
					if block.id == piece.id:
						block.x -= distance

			for block in blocklist:
				if block.id == piece.id:
					if block.y > 19:
						distance = abs(block.y - 19)
						for subblock in blocklist:
							if subblock.id == piece.id:
								subblock.y -= distance
								piece.falling = False
								piece.fallen = True
								piecefallen = True
					for subblock in blocklist:
						if subblock.x == block.x and subblock.y == block.y and subblock.id != piece.id:
							for subsubblock in blocklist:
								if subsubblock.id == piece.id:
									subsubblock.y -= 1
									piece.falling = False
									piece.fallen = True
									piecefallen = True

	if piecefallen == True and game == 'playing':
		for block in blocklist:
			if block.y < 0:
				game = 'over'
				pygame.mixer.music.load("assets/gameover.wav")
				pygame.mixer.music.play()
				with open('player_save.json', 'w') as file:
					json.dump(playerData, file, indent=4)

	if piecefallen == True and game == 'playing':
		end = False
		for block in blocklist:
			if block.y < 0:
				end = True
		if not end:
			if piecefallen == True and game == 'playing':
				for piece in pieces:
					if piece.next > 0:
						piece.next -= 1
						if piece.next == 0:
							piece.falling = True
							piece.startFall()
			piecenumber += 1
			pieces.append(Piece(random.randint(1, 7), piecenumber)) 
			holdcooldown = False

	heldblock = False
	if startfall:
		for piece in pieces:
			if piece.held == True:
				heldblock = True
		if timesheld == 1:
			for piece in pieces:
				if piece.next == 0 and piece.held == False and piece.fallen == False:
					piece.falling = True
					piece.startFall()
				startfall = False

	piecefallen = False

	counter = 0
	linecount = 0
	for row in grid:
		removelist = []
		linenotclear = False
		if 0 not in row:
			for piece in pieces:
				if piece.falling == True:
					for block in blocklist:
						if block.id == piece.id:
							if block.y == counter:
								linenotclear = True
			if linenotclear == False:
				removed = 0
				for block in blocklist:
					counter2 = 0
					if block.y == counter:
						removelist.append(block)
						removed += 1
					counter2 += 1
				if removed == 10:
					counter2 = 0
					for rem in removelist:
						blocklist.remove(rem)
						counter2 += 1
					linecount += 1
					for piece in pieces:
						if piece.falling == True:
							for block in blocklist:
								if block.id != piece.id and block.y < counter:
									block.y += 1
		counter += 1

	if linecount == 1:
		score += 100
	elif linecount == 2 or linecount == 3:
		score += 100 + (linecount - 1) * 200
	elif linecount == 4:
		score += 800

	grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

	for block in blocklist:
		block.update()

	pygame.draw.rect(window, black, (250, 0, 250, 500), 1)
	pygame.draw.rect(window, gray, (0, 0, 250, 500))
	pygame.draw.rect(window, gray, (500, 0, 250, 500))

	for y in range(0, 20):
		for x in range(0, 10):
			if grid[y][x] == 1:
				borderRect(Zred, black, x * 25 + 250, y * 25, 25, 25, 1)
				#pygame.draw.rect(window, Zred, (x * 25 + 250, y * 25, 25, 25))
				#pygame.draw.rect(window, black, (x * 25 + 250, y * 25, 25, 25), 1)
			elif grid[y][x] == 2:
				borderRect(Lorange, black, x * 25 + 250, y * 25, 25, 25, 1)
			elif grid[y][x] == 3:
				borderRect(Oyellow, black, x * 25 + 250, y * 25, 25, 25, 1)
			elif grid[y][x] == 4:
				borderRect(Sgreen, black, x * 25 + 250, y * 25, 25, 25, 1)
			elif grid[y][x] == 5:
				borderRect(Iblue, black, x * 25 + 250, y * 25, 25, 25, 1)
			elif grid[y][x] == 6:
				borderRect(Jblue, black, x * 25 + 250, y * 25, 25, 25, 1)
			elif grid[y][x] == 7:
				borderRect(Tpurple, black, x * 25 + 250, y * 25, 25, 25, 1)

	# UI shit
	scoretext = midFont.render(f'Score: {score}', False, textblack)
	window.blit(scoretext, (510, 300))
	speedtext = midFont.render(f'Speed: {60 / originalfallspeed} bps', False, textblack)
	window.blit(speedtext, (510, 340))
	speedtext = midFont.render(f'High Score: {playerData["highscore"]}', False, textblack)
	window.blit(speedtext, (510, 380))

	controls = smallFont.render('Press down to soft drop', False, textblack)
	window.blit(controls, (10, 260))
	controls = smallFont.render('Press up to hard drop', False, textblack)
	window.blit(controls, (10, 300))
	controls = smallFont.render('Press B to hold', False, textblack)
	window.blit(controls, (10, 340))
	controls = smallFont.render('Press P to pause', False, textblack)
	window.blit(controls, (10, 380))
	controls = smallFont.render('Press M to toggle music', False, textblack)
	window.blit(controls, (10, 420)) # nice

	nexttext = midFont.render("Next", False, textblack)
	holdtext = midFont.render("Hold", False, textblack)
	window.blit(nexttext, (centerText(nexttext, 70, 515), 10))
	window.blit(holdtext, (centerText(holdtext, 70, 165), 10))
	borderRect((bgRed, bgGreen, bgBlue), black, 165, 45, 70, 70, 1)
	borderRect((bgRed, bgGreen, bgBlue), black, 515, 45, 70, 70, 1)
	borderRect((bgRed, bgGreen, bgBlue), black, 515, 125, 55, 55, 1)
	borderRect((bgRed, bgGreen, bgBlue), black, 515, 190, 40, 40, 1)

	if game == 'pause':
		pauseText = largeFont.render('PAUSED', False, black)
		window.blit(pauseText, (centerText(pauseText, 750, 0), 230))

	if game == 'over':
		if bgGreen >= 5:
			bgGreen -= 5
		if bgBlue >= 5:
			bgBlue -= 5

		if gray[0] >= 53:
			gray = subtractFade(gray, (3, 3, 3))

		if textblack[0] <= 250:
			textblack = subtractFade(textblack, (-5, -5, -5))

		if endloop <= 50:
			Zred = subtractFade(Zred, RedFade)
			Lorange = subtractFade(Lorange, OrangeFade)
			Oyellow = subtractFade(Oyellow, YellowFade)
			Sgreen = subtractFade(Sgreen, GreenFade)
			Iblue = subtractFade(Iblue, CyanFade)
			Jblue = subtractFade(Jblue, BlueFade)
			Tpurple = subtractFade(Tpurple, PurpleFade)
		else:
			Zred = (0, 0, 0)
			Lorange = (0, 0, 0)
			Oyellow = (0, 0, 0)
			Sgreen = (0, 0, 0)
			Iblue = (0, 0, 0)
			Jblue = (0, 0, 0)
			Tpurple = (0, 0, 0)
		endloop += 1

		gameOverText = largeFont.render('Game Over!', False, white)
		finalScore = midFont.render(f'Your final score', False, white)
		finalScore2 = midFont.render(f'was {score}', False, white)
		GOTextSurface = gameOverText.copy()
		alphaSurface = pygame.Surface(GOTextSurface.get_size(), pygame.SRCALPHA)
		alpha = 255

		if alpha > 0:
			alpha -= 5
			GOTextSurface = gameOverText.copy()
			alphaSurface.fill((255, 255, 255, alpha))
			GOTextSurface.blit(alphaSurface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

		window.blit(finalScore, (centerText(finalScore, 750, 0), 250))
		#window.blit(finalScore, ((750 - finalScore.get_size()[0]) / 2, 250))
		window.blit(finalScore2, (centerText(finalScore, 750, 0), 280))

		window.blit(GOTextSurface, ((750 - GOTextSurface.get_size()[0]) / 2, 175))

	if score > 10000:
		originalfallspeed = 5
	elif score > 8000:
		originalfallspeed = 10
	elif score > 6000:
		originalfallspeed = 15
	elif score > 4000:
		originalfallspeed = 20
	elif score > 2000:
		originalfallspeed = 40
	else:
		originalfallspeed = 60

	if score > playerData["highscore"]:
		playerData["highscore"] = score

	for piece in pieces:
		if piece.next > 0:
			piece.color = colors[piece.piece - 1]
			piece.renderNext()
		if piece.held:
			piece.color = colors[piece.piece - 1]
			piece.renderHeld()

	if frame % fallspeed == 0 and game == 'playing':
		for piece in pieces:
			piece.update()
		if keys[pygame.K_DOWN]:
			score += 1

	frame += 1

	pygame.display.flip()

	clock.tick(60)

pygame.quit()

#Spaghetti ass code lmao
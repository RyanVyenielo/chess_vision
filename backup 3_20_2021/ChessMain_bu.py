'''
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
'''

import pygame as p
import ChessEngine
import random as rand


WIDTH = HEIGHT = 1024
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
TEXT_SIZE = 128
MAX_FPS = 15
IMAGES = {}
gs = ChessEngine.GameState()
row_name = rand.randint(0,7)
column_name = rand.randint(0,7)
name = gs.names[column_name][row_name]
name_list = []
name_list.append(name)
print(name_list)
red = (255, 0, 0)
blue = (25,25,112)
black = (0,0,0)
white = (255,255,255)
pos = (0,0)
pos_x = []
pos_y = []
link = []
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = [8, 7, 6, 5, 4, 3, 2, 1]
col = []
row = []
square = []
right = 0

for r in range(DIMENSION):
	pos_x.append([r*SQ_SIZE, r*SQ_SIZE + SQ_SIZE])
	pos_y.append([r*SQ_SIZE, r*SQ_SIZE + SQ_SIZE])

# for r in range(DIMENSION):
# 	for c in range(DIMENSION):
# 		link.append([pos_range[c], pos_range[r]]) 
# print(link)

# for r in range(DIMENSION):
# 	for c in range(DIMENSION):
# 		link.append([gs.names[r][c], pos_range[c], pos_range[r]]) 

def loadImages():
	pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
	for piece in pieces:
		IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs, name):
	drawBoard(screen)
	blink_square(name, black)
	# drawPieces(screen, gs.board)

def drawBoard(screen):
	colors = [p.Color("white"), p.Color("gray")]
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			color = colors[((r+c) % 2)]
			p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def blink_square(name, color):
	screen_text = font.render(name, True, color)
	screen.blit(screen_text,[ WIDTH/2 - SQ_SIZE/2, HEIGHT/2 - SQ_SIZE/2])



#This function's purpose is highlight a square when you click on it and show the name of the square

def drawPieces(screen, board):
	for r  in range(DIMENSION):
		for c in range(DIMENSION):
			piece = board[r][c]
			if piece != "--":
				screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# def position_check(names, pos):
# 	for r  in range(DIMENSION):
# 			for c in range(DIMENSION):
# 				square = names[r][c]
# 				if square == :
# 					screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
n = 1
nd = 1
num_clicks = 0
p.init()
font = p.font.SysFont(None, TEXT_SIZE)
p.display.set_caption("Vision Practice")
screen = p.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()
screen.fill(p.Color("white"))
loadImages()
running = True
while running:
	for e in p.event.get():
		
		if e.type == p.QUIT:
			running == False
		if e.type == p.MOUSEBUTTONUP:
			row_name = rand.randint(0,7)
			column_name = rand.randint(0,7)
			name = gs.names[column_name][row_name]
			name_list.append(name)
			print(name_list)
			pos = p.mouse.get_pos()
			n = 1
			nd = 1
			num_clicks = num_clicks + 1
			print(num_clicks)
			print("pos:")
			print(pos)
			
		while n == 1:
			for r in range(DIMENSION):
				if pos_x[r][0] <= pos[0] <= pos_x[r][1]: 
					print(pos_x[r])
					print("pos_x:")
					print(r)
					square.append(str(columns[r]))

			for r in range(DIMENSION):
				if pos_y[r][0] <= pos[1] <= pos_y[r][1]:
					print(pos_y[r])
					print("pos_y:")
					print(r)
					square.append(str(rows[r]))
			n = 0

					
			x = square[2*num_clicks]
			y = square[2*num_clicks+1]
			z = x + y
			square_length = len(square)
			squares_so_far = int(square_length/2) - 1
			if z == name_list[num_clicks - 1]:
				print("Correct")
				right = right + 1

			print("x:" + str(x))
			print("y:" + str(y))
			print("z:" + str(z))
			print("name:" + name)
			print("Total Right:" + str(right) + "/" + str(squares_so_far))
			print(square)
		
	drawGameState(screen, gs, name)		
	clock.tick(MAX_FPS)
	p.display.flip()

# if __name__ == "__main__":
# 	main()





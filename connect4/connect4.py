import numpy as np
# import random
from .minimax import *
from .state import *
from .constants import *
import pygame
import sys
import math
turn_count = 0


def create_board():
	b = np.zeros((NUM_OF_ROWS, NUM_OF_COLS))
	return b


def draw_board():
	for r in range(NUM_OF_ROWS):
		for c in range(NUM_OF_COLS):
			pygame.draw.rect(surface, BLUE, (c*SQUARE, r*SQUARE+SQUARE, SQUARE, SQUARE))
			pygame.draw.circle(surface, BLACK, (int(c * SQUARE + SQUARE / 2), int(r * SQUARE + SQUARE + SQUARE / 2)), CIRCLE)
	pygame.display.update()

	for r in range(NUM_OF_ROWS):
		for c in range(NUM_OF_COLS):
			if board[r][c] == 1:
				pygame.draw.circle(surface, YELLOW, (int(c*SQUARE+SQUARE/2), height + SQUARE - int(r*SQUARE+SQUARE+SQUARE/2)), CIRCLE)
			elif board[r][c] == 2:
				pygame.draw.circle(surface, RED, (int(c*SQUARE+SQUARE/2), height + SQUARE - int(r*SQUARE+SQUARE+SQUARE/2)), CIRCLE)
	pygame.display.update()


def message_display(text):
	myfont = pygame.font.SysFont('monospace', 75)
	text_surface = myfont.render(text, True, RED)
	surface.blit(text_surface, (40, 10))


def is_legal_move(col):
	if available_row(col) is not None:
		return True
	return False


def make_move(mv, player):
	if is_legal_move(mv):
		board[available_row(mv)][mv] = player
		if player == 1:
			opponent = 2
		else:
			opponent = 1
		return State(board, opponent)
	return None


def available_row(col):
	for r in range(NUM_OF_ROWS):
		if board[r][col] == 0:
			return r


board = create_board()


pygame.init()

width = NUM_OF_COLS * SQUARE
height = NUM_OF_ROWS * SQUARE + SQUARE
surface_size = (width, height)
surface = pygame.display.set_mode(surface_size)

draw_board()
pygame.display.update()

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if turn_count % 2 == 0:
			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(surface, BLACK, (0, 0, NUM_OF_COLS * SQUARE, SQUARE))
				pygame.draw.circle(surface, RED, (event.pos[0], 50), CIRCLE)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(surface, BLACK, (0, 0, NUM_OF_COLS * SQUARE, SQUARE))
				move = int(math.floor(event.pos[0] / SQUARE))
				if is_legal_move(move):
					new_state = make_move(move, 2)
					pygame.display.update()
					turn_count += 1
					draw_board()
					if new_state.check_if_won(2):
						message_display('You Win')
						pygame.display.update()
						game_over = True
						pygame.time.wait(3000)

		else:
			m = Minimax(State(board, 1))
			move = m.get_best_move()
			new_state = make_move(move, 1)
			turn_count += 1
			draw_board()
			if new_state.check_if_won(1):
				message_display('You Lose')
				pygame.display.update()
				game_over = True
				pygame.time.wait(3000)

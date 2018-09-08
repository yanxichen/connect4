import numpy as np
import random
from .constants import *


class State:

	def __init__(self, board, player):
		self.board = board
		self.legal_moves = []
		self.populate_legal_moves()
		self.player = player

	def check_streak(self, player, streak):
		count = 0
		v_visited = set()
		h_visited = set()
		dl_visited = set()
		dr_visited = set()
		board = self.board

		def check_vertical(r, c, visited, i):
			if r < NUM_OF_ROWS and (r, c) not in visited and board[r][c] == player:
				if i >= streak:
					return 1
				else:
					visited.add((r, c))
					return check_vertical(r + 1, c, visited, i + 1)
			else:
				return 0

		def check_horizontal(r, c, visited, i):
			if c < NUM_OF_COLS and (r, c) not in visited and board[r][c] == player:
				if i >= streak:
					visited.add((r, c))
					return 1
				else:
					visited.add((r, c))
					return check_horizontal(r, c + 1, visited, i + 1)
			else:
				return 0

		def check_r_diagonal(r, c, visited, i):
			if r < NUM_OF_ROWS and c < NUM_OF_COLS and (r, c) not in visited and board[r][c] == player:
				if i >= streak:
					visited.add((r, c))
					return 1
				else:
					visited.add((r, c))
					return check_r_diagonal(r + 1, c + 1, visited, i + 1)
			else:
				return 0

		def check_l_diagonal(r, c, visited, i):
			if r < NUM_OF_ROWS and 0 <= c < NUM_OF_COLS and (r, c) not in visited and board[r][c] == player:
				if i >= streak:
					visited.add((r, c))
					return 1
				else:
					visited.add((r, c))
					return check_l_diagonal(r + 1, c - 1, visited, i + 1)
			else:
				return 0

		for ro in range(NUM_OF_ROWS):
			for col in range(NUM_OF_COLS):
				count += check_vertical(ro, col, v_visited, 1)
				count += check_horizontal(ro, col, h_visited, 1)
				count += check_r_diagonal(ro, col, dr_visited, 1)
				count += check_l_diagonal(ro, col, dl_visited, 1)
		return count

	def get_score(self):
		if self.check_streak(2, 4) > 0:
			return -100000
		else:
			return 100000 * self.check_streak(1, 4) + 100 * self.check_streak(1, 3)
			# + 10 * self.check_streak(1, 2)

	def populate_legal_moves(self):
		for i in range(NUM_OF_COLS):
			if self.available_row(i) is not None:
				self.legal_moves.append(int(i))

	def available_row(self, col):
		for r in range(NUM_OF_ROWS):
			if self.board[r][col] == 0:
				return r

	def check_if_won(self, player):
		if self.check_streak(player, 4) > 0:
			return True
		return False

	def make_move(self, move):
		if self.player == 1:
			opponent = 2
		else:
			opponent = 1
		new_board = np.copy(self.board)
		new_board[self.available_row(move)][move] = self.player
		return State(new_board, opponent)


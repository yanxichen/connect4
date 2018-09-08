from .state import *


class Minimax:

	def __init__(self, state):
		self.state = state

	def alphabeta(self, state, depth, alpha, beta):
		if depth == 0 or state.check_if_won(1) or state.check_if_won(2):
			return state.get_score()
		elif state.player == 1:
			score = -999999
			for move in state.legal_moves:
				new_state = state.make_move(move)
				score = max(score, self.alphabeta(new_state, depth - 1, alpha, beta))
				alpha = max(alpha, score)
				if alpha >= beta:
					break
			return score
		else:
			score = 999999
			for move in state.legal_moves:
				new_state = state.make_move(move)
				score = min(score, self.alphabeta(new_state, depth - 1, alpha, beta))
				beta = min(beta, score)
				if alpha >= beta:
					break
			return score

	def get_best_move(self):
		best_score = -999999
		best_move = None

		for move in self.state.legal_moves:
			new_state = self.state.make_move(move)
			score = self.alphabeta(new_state, DEPTH, -999999, 999999)
			if score > best_score:
				best_score = score
				best_move = move

		return best_move

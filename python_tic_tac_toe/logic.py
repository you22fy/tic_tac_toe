"""logic.py"""

import random

class TicTacToe:
    def __init__(self):
        self.game = [''] * 9  # 9つの空のスロット
        self.player = 'X'  # 最初のプレーヤーは 'X'

    def check_winner(self):
        # 勝利のパターン
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
        
        for a, b, c in wins:
            if self.game[a] == self.game[b] == self.game[c] != '':
                return self.game[a], (a, b, c)
        if '' not in self.game:
            return 'Tie', ()
        return None, ()

    def make_move(self, index):
        if self.game[index] == '':
            self.game[index] = self.player
            self.player = 'O' if self.player == 'X' else 'X'

    def get_available_moves(self):
        return [i for i, x in enumerate(self.game) if x == '']

    def cpu_move(self):
        available_moves = self.get_available_moves()
        if available_moves:
            move = random.choice(available_moves)
            self.make_move(move)

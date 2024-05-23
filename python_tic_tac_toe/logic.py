"""logic.py"""

import random


class TicTacToeLogic:
    """Tic Tac Toe ゲームのロジックを管理する."""

    def __init__(self):
        """classのinitializerです。インスタンスの生成時に実行されます"""
        #  NOTE: 盤面を拡張してオセロなどの他のゲームをサポートするには2次元リストに変更する方が良いかもしれません.(Future work)
        self.game = [""] * 9
        self.player = "X"  # Xが先手

    def check_winner(self):
        """
        勝敗をチェックするメソッド.

        Returns
        -------
        str
            勝者がいる場合は、勝者の名前(X or O)を返します。引き分けの場合は'Tie'を返します。
            それ以外の場合はNoneを返します。
        tuple
            勝者がいる場合は、勝利したラインを返します。それ以外の場合は空のタプルを返します。
        """
        # 3目並べの勝利条件は以下の通りであることが知られている.
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in wins:
            if self.game[a] == self.game[b] == self.game[c] != "":
                return self.game[a], (a, b, c)
        if "" not in self.game:
            return "Tie", ()
        return None, ()

    def make_move(self, index: int):
        """
        プレーヤーが指定したインデックスにマークを置くメソッド.

        Parameters
        ----------
        index : int
            プレーヤーがマークを置くインデックス
        """

        if self.game[index] == "":
            self.game[index] = self.player
            self.player = "O" if self.player == "X" else "X"

    def cpu_move(self):
        """
        CPUの手を決めるメソッド.
        開いているマスの中からランダムに選択する.
        """
        available_moves = [i for i, x in enumerate(self.game) if x == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.make_move(move)

"""app.py"""

import tkinter as tk
from tkinter import messagebox, font
from logic import TicTacToeLogic


class TicTacToeApp:
    """Tic Tac Toe ゲームのGUIを管理します。Tkinterを使用しています。"""

    def __init__(self, root):
        """classのinitializerです。インスタンスの生成時に実行されるメソッド."""
        self.root = root
        self.root.title("三目並べ")
        self.game = TicTacToeLogic()
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        """ゲームボードのボタンを作成するメソッド."""
        game_font = font.Font(size=24, weight="bold")
        for i in range(9):
            button = tk.Button(
                self.root,
                text="",
                font=game_font,
                width=5,
                height=2,
                command=lambda i=i: self.on_click(i),
            )
            button.grid(
                row=i // 3,
                column=i % 3,
                sticky="nsew",
            )
            self.buttons.append(button)
            self.root.grid_rowconfigure(i // 3, weight=1)
            self.root.grid_columnconfigure(i % 3, weight=1)

    def on_click(self, index):
        """ボタンがクリックされたときの処理を行うメソッド."""
        if self.game.game[index] == "" and not self.game.check_winner()[0]:
            self.game.make_move(index)
            self.update_board()
            winner, _ = self.game.check_winner()
            if winner:
                self.root.after(100, self.check_game_over)
            elif not winner:
                self.root.after(500, self.cpu_turn)

    def cpu_turn(self):
        """CPUのターンを実行するメソッド."""
        self.game.cpu_move()
        self.update_board()
        winner, _ = self.game.check_winner()
        if winner:
            self.root.after(100, self.check_game_over)

    def update_board(self):
        """ボードの状態を更新するメソッド."""
        for i in range(9):
            self.buttons[i].config(text=self.game.game[i])

    def check_game_over(self):
        """ゲームが終了したかどうかを確認するメソッド."""
        winner, _ = self.game.check_winner()
        if winner:
            self.show_winner(winner)

    def show_winner(self, winner):
        """勝者ダイアログを表示するメソッド."""
        result = "引き分け" if winner == "Tie" else f"勝者: {winner}"
        messagebox.showinfo("ゲーム終了", result)
        self.reset()

    def reset(self):
        """ゲームの盤面をリセットするメソッド."""
        self.game = TicTacToeLogic()
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")

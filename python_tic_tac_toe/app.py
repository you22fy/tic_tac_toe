"""app.py"""

import tkinter as tk
from tkinter import messagebox, font
from logic import TicTacToe

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title('三目並べ')
        self.game = TicTacToe()
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        game_font = font.Font(size=24, weight="bold")
        for i in range(9):
            button = tk.Button(self.root, text='', font=game_font, width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3, sticky="nsew")
            self.buttons.append(button)
            self.root.grid_rowconfigure(i//3, weight=1)
            self.root.grid_columnconfigure(i%3, weight=1)
            button.config(bg='light blue')

    def on_click(self, index):
        if self.game.game[index] == '' and not self.game.check_winner()[0]:
            self.game.make_move(index)
            self.update_board()
            # 次はCPUのターン
            if not self.game.check_winner()[0]:
                self.root.after(500, self.cpu_turn)

    def cpu_turn(self):
        self.game.cpu_move()
        self.update_board()
        winner, _ = self.game.check_winner()
        if winner:
            self.root.after(100, self.check_game_over)  # 画面更新後にゲーム結果を確認

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.game.game[i])

    def check_game_over(self):
        winner, winning_line = self.game.check_winner()
        if winner:
            self.highlight_winner(winning_line)
            self.show_winner(winner)

    def highlight_winner(self, winning_line):
        for index in winning_line:
            self.buttons[index].config(bg='yellow')

    def show_winner(self, winner):
        result = '引き分け' if winner == 'Tie' else f'勝者: {winner}'
        messagebox.showinfo("ゲーム終了", result, icon='info')
        self.reset()

    def reset(self):
        self.game = TicTacToe()
        for button in self.buttons:
            button.config(text='', bg='light blue')

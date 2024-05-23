"""main.py"""

import tkinter as tk
from app import TicTacToeApp


def main():
    """プログラムのエントリーポイント."""
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

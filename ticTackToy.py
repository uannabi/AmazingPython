
import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.resizable(False, False)

        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.turn = 1

        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, width=10, height=4, command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)

    def play(self, i, j):
        
        if self.board[i][j] != 0:
            return

        if self.turn == 1:
            button = tk.Label(text="x",font=('Arial', 25))
            button.grid(row=i, column=j)
            self.board[i][j] = 1
            self.turn = 2
        else:
            button = tk.Label(text="o",font=('Arial', 25))
            button.grid(row=i, column=j)
            self.board[i][j] = 2
            self.turn = 1

        self.check_winner()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.end_game(self.board[i][0])
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.end_game(self.board[0][i])
                return

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.end_game(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.end_game(self.board[0][2])
            return

    def end_game(self, winner):
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.destroy()

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()




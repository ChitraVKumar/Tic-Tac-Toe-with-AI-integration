import tkinter as tk
from tkinter import messagebox

class Board:
    def __init__(self, master, click_action):
        self.master = master #This line stores the master parameter in an instance variable so it can be used elsewhere.the master widget is the main window where board will be placed.
        # self.cells = [[None for _ in range(3)] for _ in range(3)]
        
        self.cells = []
        for _ in range(3):  # Outer loop: responsible for creating each row
            row = []
            for _ in range(3):  # Inner loop: responsible for filling each row with 'None'
                row.append(None)
            self.cells.append(row)

        self.create_board(click_action)

    def create_board(self, click_action):
        for row in range(3):
            for col in range(3):
                self.cells[row][col] = tk.Button(self.master, text='', font=('normal', 40), height=2, width=4, command= lambda r=row, c= col: click_action(r, c))
                self.cells[row][col].grid(row=row, column=col)

def test_click(row, col):
    print(f"Button at {row}, {col} clicked.")


if __name__ == "__main__":
    root = tk.Tk()
    board = Board(root, test_click)
    root.mainloop()
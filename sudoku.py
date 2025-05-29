import tkinter as tk

# Create the Sudoku board (9x9)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(board, row, col, num):
    """Check if placing num in board[row][col] is valid."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

def solve(board):
    """Backtracking algorithm to solve Sudoku."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0  # Reset if solution fails
                return False
    return True

def display_solution():
    """Solve Sudoku and update GUI."""
    if solve(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(tk.END, str(board[i][j]))

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

entries = [[tk.Entry(root, width=2, font=("Arial", 24), justify="center") for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j)
        if board[i][j] != 0:
            entries[i][j].insert(tk.END, str(board[i][j]))

solve_button = tk.Button(root, text="Solve", font=("Arial", 14), command=display_solution)
solve_button.grid(row=10, column=4)

root.mainloop()
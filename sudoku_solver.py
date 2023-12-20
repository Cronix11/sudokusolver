import math


def outside_square(current):
    return [x for x in range(9) if x not in range(3 * current, 3 * current + 3)]


def inside_square(current):
    return [x for x in range(3 * current, 3 * current + 3)]


def clear_row(num_row, num_col, puzzle):
    # Clear the row not inside the current square
    num = puzzle[num_row][num_col]
    current_col = math.floor(num_col / 3)
    cols_list = outside_square(current_col)
    for col in cols_list:
        if isinstance(puzzle[num_row][col], list):
            try:
                puzzle[num_row][col].remove(num)
            except ValueError:
                None


def clear_col(num_row, num_col, puzzle):
    # Clear the col not in current square
    num = puzzle[num_row][num_col]
    current_row = math.floor(num_row / 3)
    rows_list = outside_square(current_row)
    for row in rows_list:
        if isinstance(puzzle[row][num_col], list):
            try:
                puzzle[row][num_col].remove(num)
            except ValueError:
                None


def clear_square(num_row, num_col, puzzle):
    # Clear the current square
    num = puzzle[num_row][num_col]
    current_row, current_col = math.floor(num_row / 3), math.floor(num_col / 3)
    rows_list = inside_square(current_row)
    cols_list = inside_square(current_col)
    for row in rows_list:
        for col in cols_list:
            if isinstance(puzzle[row][col], list):
                try:
                    puzzle[row][col].remove(num)
                except ValueError:
                    None


def sudoku(puzzle):
    # Change all zeros into list of posibilities
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                puzzle[row][col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solved = False
    for _ in range(50):
        # while solved != True:
        solved = True
        # Iterate all squares
        for row in range(9):
            for col in range(9):
                # If its a one length list turn it into an int
                if isinstance(puzzle[row][col], list):
                    solved = False
                    if len(puzzle[row][col]) == 1:
                        puzzle[row][col] = puzzle[row][col][0]
                        solved = True
                else:
                    clear_row(row, col, puzzle)
                    clear_col(row, col, puzzle)
                    clear_square(row, col, puzzle)
    return puzzle


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

print(sudoku(puzzle) == solution)

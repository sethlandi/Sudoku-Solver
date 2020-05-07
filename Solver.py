# solver.pnumber

# Hard coding board in for now
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],  # Row; not block
    [6, 0, 0, 0, 8, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 3, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


# For now just print hard coded board
def format_board(board):
    row = len(board)
    for y in range(row):  # Created loose for cube
        space = "  "  # Reset
        if y % 3 == 0 and y != 0:  # Prints x-axis spaces on board (eg after 3 and 6; not at start)
            print(space)

        for x in range(len(board[y])):
            import pdb; pdb.set_trace()
            control_char = ("\n" if x == 8 else space)  # Changes the control character to \n or not
            is_space = (space if x % 3 == 0 and x != 0 else "")

            print(is_space + str(board[y][x]), end=control_char)


def possible(board):
    row = len(board)
    for y in range(row):
        import pdb; pdb.set_trace()
        for x in range(len(board[y])):
            if board[y][x] == 0:
                for n in range(min(board) + 1, max(board) + 1):
                    board[y][x] = n
                    valid(board, x, y, n)
                    board[y][x] = 0


# y = col, x = row, n = num
def valid(board, y, x, n):
    for i in range(len(board)):  # ONLY WORKS FOR SQUARES!
        if board[y][i] == n or board[i][x] == n:  # Checks rows and columns
            return False

    y_box = (y // 3) * 3
    x_box = (x // 3) * 3

    for i in range(y_box, y_box + 3):
        for j in range(x_box, x_box + 3):
            if board[y_box + i][x_box + j] == n:
                return False
        return None


format_board(board)
print("")
possible(board)

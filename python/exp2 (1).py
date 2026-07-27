N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

if solve(board, 0):
    print("Solution:")
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
else:
    print("No solution exists.")

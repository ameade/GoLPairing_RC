import copy
def progress_board(old_board):
    new_board = copy.deepcopy(old_board)
    for row in range(len(new_board)):
        for col in range(len(new_board[row])):
            count = count_neighbors(old_board, row, col)
            # rule 1
            if count < 2:
                new_board[row][col] = False

    return new_board

def count_neighbors(board, row, col):
    count = 0
    neighborhood = get_neighborhood(board, row, col)
    for board_row in neighborhood:
        for board_cell in board_row:
            if board_cell:
                count += 1

    if board[row][col]:
        count -= 1
    return count

def get_neighborhood(board, row, col):
    neighborhood = [[False, False, False], [False, False, False], [False, False, False]]
    for row_modifier in (-1, 0, 1):
        for col_modifier in (-1, 0, 1):
            neighborhood[row_modifier+1][col_modifier+1] = board[row + row_modifier][col + col_modifier]
    return neighborhood

if __name__ == "__main__":
    pass
import numpy as np
old_board = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]])
board = old_board.copy()

def find_block(row,column):
    if row < 3:
        if column < 3:
            return 1
        elif column >= 3 and column < 6:
            return 2
        elif column >= 6 and column < 9:
            return 3
    elif row >= 3 and row < 6:
        if column < 3:
            return 4
        elif column >= 3 and column < 6:
            return 5
        elif column >= 6 and column < 9:
            return 6
    elif row >= 6 and row <= 9:
        if column < 3:
            return 7
        elif column >= 3 and column < 6:
            return 8
        elif column >= 6 and column < 9:
            return 9

def find_row(entry_index):
    puzzle_rows = board.shape[0]
    if entry_index in range(0, puzzle_rows):
        return board[entry_index]

def find_column(entry_index):
    puzzle_columns = board.shape[1]
    if entry_index in range(0, puzzle_columns ):
        return board[0:puzzle_columns, entry_index]


def empty_indexes():
    empty = np.where(board == 0)
    locations = np.dstack((empty[0], empty[1]))
    all_empty_locations = []
    for i in locations[0]:
        row = i[0]
        column = i[1]
        all_empty_locations.append([row, column])

    return all_empty_locations

def puzzle_to_block(block_number):
    if block_number <= 3:
        i, j = 0, 3
        k = 3 * (block_number - 1)
        h = 3 * (block_number)
        return board[i:j, k:h]
    elif block_number > 3 and block_number <= 6:
        i, j = 3, 6
        k = 3 * ((block_number - 3) - 1)
        h = 3 * (block_number - 3)
        return board[i:j, k:h]
    elif block_number > 6 and block_number <= 9:
        i, j = 6, 9
        k = 3 * ((block_number - 6) - 1)
        h = 3 * (block_number - 6)
        return board[i:j, k:h]

def find_intersection(row,column,block):
    row_possibility = []
    column_possibility = []
    block_possibility = []

    for j in range(1, 10):  # here we find the values that our empty position can accept.
        if j not in find_row(row):
            row_possibility.append(j)
        if j not in find_column(column):
            column_possibility.append(j)
        if j not in puzzle_to_block(block):
            block_possibility.append(j)
    intersection_of_all_elements = list(
        set.intersection(*map(set, [row_possibility, column_possibility, block_possibility])))
    return intersection_of_all_elements


def sudoku_solver(counter=0):
    if 0 not in board:
        print('DONE:')
        print(board)
    else:
        all_empty_locations  = empty_indexes()[counter-1]
        block = find_block(all_empty_locations[0], all_empty_locations[1])
        index_info = (all_empty_locations , block)
        row = index_info[0][0]
        column = index_info[0][1]
        index_block = index_info[1]
        intersection_of_elements = find_intersection(row,column,index_block)
        if len(intersection_of_elements) == 1:

            right_value = intersection_of_elements[0]
            board[row , column ] = right_value
            return sudoku_solver(0)
        else:
            counter +=1
            return sudoku_solver(counter)


if __name__ == '__main__':
    print('input:\n',board)
    print('answer: \n')
    sudoku_solver()

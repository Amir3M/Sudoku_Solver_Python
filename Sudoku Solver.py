import numpy as np
# array below is our main puzzle that you can chnage it.
puzzle = [[9,7,0,0,4,1,0,0,6],
                [0,0,0,0,7,0,5,0,9],
                [0,0,6,0,0,0,0,8,1],
                [0,0,0,2,8,7,4,0,0],
                [7,6,3,0,1,5,8,0,0],
                [2,8,4,0,3,0,1,5,7],
                [0,4,0,0,0,2,9,7,8],
                [0,2,5,7,9,8,0,1,4],
                [8,0,7,0,6,0,3,0,0]]
my_puzzle = np.array(puzzle)

def block(num):
    if num <= 3:
        i, j = 0, 3
        k = 3 * (num-1)
        h = 3 * (num)
        return my_puzzle[i:j, k:h]
    elif num > 3 and num <= 6:
        i, j = 3, 6
        k = 3 * ((num-3)-1)
        h = 3 * ((num-3))
        return my_puzzle[i:j, k:h]
    elif num > 6 and num <= 9:
        i, j = 6, 9
        k = 3 * ((num-6)-1)
        h = 3 * ((num-6))
        return my_puzzle[i:j, k:h]

def row(num):
    rows = my_puzzle.shape[0]
    if num in range(1, (rows+1)):
        return my_puzzle[num -1]

def column(num):
    columns = my_puzzle.shape[1]
    if num in range(1, (columns+1)):
        i = num -1
        return my_puzzle[0:columns, i]

def block_finder(row, column):
    if row <= 3:
        if column <= 3:
            return 1
        elif column > 3 and column <= 6:
            return 2
        elif column > 6 and column <= 9:
            return 3
    elif row > 3 and row <= 6:
        if column <= 3:
            return 4
        elif column > 3 and column <= 6:
            return 5
        elif column > 6 and column <= 9:
            return 6
    elif row > 6 and row <= 9:
        if column <= 3:
            return 7
        elif column > 3 and column <= 6:
            return 8
        elif column > 6 and column <= 9:
            return 9

def emptys(num):
    empty = np.where(my_puzzle == 0)
    locations = np.dstack((empty[0], empty[1]))
    all = []
    for i in locations[0]:
        row = i[0] + 1
        column = i[1] + 1
        all.append([row, column])
    block = block_finder(all[num-1][0], all[num-1][1])
    if num == 0:
        return len(all)
    else: 
        return all[num-1], block

        
while 0 in my_puzzle:
    for i in range(1, (emptys(0)+1)): # this loop works as long as we have '0' in table
        print(emptys(0))
        info = emptys(i)# each '0' in table has an address that includes row_number, column_number and block number
        R = info[0][0]  # Row
        C = info[0][1]  # column
        B = info[1]     # block
        RP = []
        CP = []
        BP = []
        for j in range(1, 10):  # here we find the values that our empty position can accept.
            if j not in row(R):
                RP.append(j)
            if j not in column(C):
                CP.append(j)
            if j not in block(B):
                BP.append(j)
        elements_in_all = list(set.intersection(*map(set, [RP, CP, BP])))   # in this list we store the values that we found
        print(f'Empty number[{i}]can contain: ',elements_in_all)
        if len(elements_in_all) == 1 :  # if there was only one possible value, we'll insert it in that position
            print('***right Value founded!***')
            right_value = elements_in_all[0]
            my_puzzle[R-1, C-1] = right_value
            print(my_puzzle)
            break
print('Done!')
last = []
for i in my_puzzle:
    last.append(list(i))
print(last)
print(type(last))
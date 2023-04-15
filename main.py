# Board stored as a 2D array
sudokuBoard = [[0, 7, 0, 0, 2, 0, 0, 4, 6],
 [0, 6, 0, 0, 0, 0, 8, 9, 0],
 [2, 0, 0, 8, 0, 0, 7, 1, 5],
 [0, 8, 4, 0, 9, 7, 0, 0, 0],
 [7, 1, 0, 0, 0, 0, 0, 5, 9],
 [0, 0, 0, 1, 3, 0, 4, 8, 0],
 [6, 9, 7, 0, 0, 2, 0, 0, 8],
 [0, 5, 8, 0, 0, 0, 0, 6, 0],
 [4, 3, 0, 0, 8, 0, 0, 7, 0]]

# print out formatted grid
def print_grid():
    for i in range(0, 9, 3):
        for k in range(i, i+3):
            for j in range(0, 9):
                if j != 0 and j % 3 == 0:
                    print("|", end=" ")
                if (sudokuBoard[k][j] == 0):
                    print(" ", end=" ")
                else:
                    print(sudokuBoard[k][j], end=" ")
            print("")
        print("- - - - - - - - - - -")

# Function for finding next empty spot
def find_empty():
    for i in range(0, 9):
        for j in range(0, 9):
            if sudokuBoard[i][j] == 0:
                return (j, i)
    return False

# Find if a number is possible in given spot
def is_possible(x, y, actual):
    for i in range(0, 9):
        if sudokuBoard[i][x] == actual or sudokuBoard[y][i] == actual:
            return False
    box_x = x // 3
    box_y = y // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if sudokuBoard[i][j] == actual:
                return False
    return True

# Recursive solver
def solve():
    find = find_empty()
    if find == False:
        print_grid()
        return
    for i in range(1, 10):
        if is_possible(find[0], find[1], i):
            sudokuBoard[find[1]][find[0]] = i
            if solve():
                return True
            sudokuBoard[find[1]][find[0]] = 0
    return False


print_grid()
solve()
print("")
print("")
print_grid()


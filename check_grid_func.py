"""

The purpose of this script is to validate the solution of a sudoku solver as a cross-check.

@author: Akus C.
"""

def check_grid_func(grid, row, col):
    val = grid[row][col];
    grid[row][col] = 0;
    
    grid_alt = [*zip(*grid)]; # Transposes grid input
    
    # Checks row and column for duplicate number
    if val in grid_alt[col] or val in grid[row]:
        grid[row][col] = val;
        print('Error at Value: %d, row: %d, col: %d' %(val, row, col))
        return
    
    # Check the 3 by 3 box for a duplicate number
    init_col = col - col % 3;
    init_row = row - row % 3;
    sliced_grid = [col[init_col:init_col+3] for col in grid][init_row:init_row+3];

    for i in range(3):
        if val in sliced_grid[i]:
            grid[row][col] = val;
            print('Error at Value: %d, row: %d, col: %d' %(val, row, col))
            return
    grid[row][col] = val;
    return
    # Returns true if the value is not in the row, col, or sub 3x3 box


def check_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            check_grid_func(grid, i, j)

grid = [[3, 1, 5, 6, 2, 7, 4, 9, 8],
        [6, 2, 4, 1, 9, 8, 3, 5, 7],
        [9, 8, 7, 5, 3, 4, 2, 1, 6],
        [1, 4, 3, 9, 6, 2, 7, 8, 5],
        [2, 7, 6, 8, 5, 3, 1, 4, 9],
        [5, 9, 8, 4, 7, 1, 6, 2, 3],
        [7, 5, 1, 3, 4, 9, 8, 6, 2],
        [8, 3, 9, 2, 1, 6, 5, 7, 4],
        [4, 6, 2, 7, 8, 5, 9, 3, 1]];

# 3 1 5 6 2 7 4 9 8
# 6 2 4 1 9 8 3 5 7
# 9 8 7 5 3 4 2 1 6
# 1 4 3 9 6 2 7 8 5
# 2 7 6 8 5 3 1 4 9
# 5 9 8 4 7 1 6 2 3
# 7 5 1 3 4 9 8 6 2
# 8 3 9 2 1 6 5 7 4
# 4 6 2 7 8 5 9 3 1

check_grid(grid)
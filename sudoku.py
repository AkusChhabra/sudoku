"""

The purpose of this project is to solve a sudoku puzzle.

1) Check numbers in rows are unique
2) Check numbers in columns are unique
3) Check numbers in 3x3 are unique

@author: Akus C.
"""

# Input Grid
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]];

# grid = [[3, 0, 0, 0, 2, 0, 4, 0, 0],
#         [0, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 3, 9, 0, 0, 0, 0, 0],
#         [0, 7, 0, 8, 0, 3, 1, 0, 0],
#         [0, 0, 0, 4, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 9, 0, 0, 0],
#         [8, 0, 9, 0, 0, 0, 0, 0, 4],
#         [4, 0, 0, 0, 0, 0, 0, 0, 0]];

# Check if numbers satisfy rules of sudoku
def check_validity(grid, row, col, val):
    grid_alt = [*zip(*grid)]; # Transposes grid input
    
    # Checks row and column for duplicate number
    if val in grid_alt[col] or val in grid[row]:
        return False
    
    # Check the 3 by 3 box for a duplicate number
    init_col = col - col % 3;
    init_row = row - row % 3;

    sliced_grid = [col[init_col:init_col+3] for col in grid][init_row:init_row+3];
    
    for i in range(3):
        if val in sliced_grid[i]: 
            return False
        
    # Returns true if the value is not in the row, col, or sub 3x3 box
    return True
        

def fill_element(grid, row, col):
    ## Check for extremities
    # Check if last column has been attained to move to the next row
    if col == 9:
        # Go back to first column and go one row up once last column is checked
        col = 0;
        row += 1;
    ## Exit condition
    if col == 0 and row == 9:
        return True
    
    # Check if the number is greater than 0
    if grid[row][col] > 0:
        # Go to the next column if number is greater than 0
        return fill_element(grid, row, col+1)
    for val in range(1, 10):
        if check_validity(grid, row, col, val):
            grid[row][col] = val;
            # Check subsequent empty positions to ensure value is valid
            if fill_element(grid, row, col+1):
                return True
        # Replace positional value to zero if the assumed value is not correct
        grid[row][col] = 0;
    return False


# Print grid out to console
def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])

# Call recursive function and print solution
def sudoku(grid):
    # fill_element(grid, 0, 0)
    # print_grid(grid)
    if fill_element(grid, 0, 0):
        print_grid(grid)
    else:
        print("Not a valid puzzle")
# Call sudoku function
sudoku(grid)



    
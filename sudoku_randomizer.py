"""

Sudoku Puzzle Randomizer

@author: Akus C.
"""

from check_grid_func import check_grid
from sudoku import sudoku_init
from random import shuffle
import copy

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

def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])

## Declarations

grid = [[3, 1, 5, 6, 2, 7, 4, 9, 8],
        [6, 2, 4, 1, 9, 8, 3, 5, 7],
        [9, 8, 7, 5, 3, 4, 2, 1, 6],
        [1, 4, 3, 9, 6, 2, 7, 8, 5],
        [2, 7, 6, 8, 5, 3, 1, 4, 9],
        [5, 9, 8, 4, 7, 1, 6, 2, 3],
        [7, 5, 1, 3, 4, 9, 8, 6, 2],
        [8, 3, 9, 2, 1, 6, 5, 7, 4],
        [4, 6, 2, 7, 8, 5, 9, 3, 1]];

# Copy grid list to another variable
shuff_list = copy.copy(grid);

# Create a list of indices from 0 to 80 and shuffle them
vals = [x for x in range(1, len(grid)*len(grid[1]))]
shuffle(vals)
vals = vals[0:int(len(vals)*0.3)]

# Remove values from grid based on randomized indices
for ind in range(len(vals)):
    # Define current index
    row = vals[ind] % 9;
    col = vals[ind] // 9;
    
    # Copy the value at the location in case of accidental removal
    hold_val = copy.deepcopy(shuff_list[row][col]);
    temp = copy.deepcopy(shuff_list);
    
    # Set value of shuffled list position to zero
    temp[row][col] = 0;
    if fill_element(temp, 0, 0):
        val = shuff_list[row][col];
        shuff_list[row][col] = 0;
        temp = copy.deepcopy(shuff_list);
    else:
        temp = shuff_list;
        continue

print('\n Print Result')
print_grid(temp)


print('\n Call Sudoku: ')
hold = copy.deepcopy(sudoku_init(temp))


print('\n Check Grid Validity:')
check_grid(temp)


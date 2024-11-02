"""

Sudoku Puzzle Randomizer

@author: Akus C.
"""

from sudoku import sudoku
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

grid = [[3, 1, 6, 5, 2, 8, 4, 9, 7],
        [5, 2, 1, 3, 4, 7, 8, 6, 9],
        [2, 8, 7, 6, 5, 4, 9, 3, 1],
        [6, 4, 3, 9, 1, 5, 7, 8, 2],
        [9, 7, 2, 8, 6, 3, 1, 4, 5],
        [7, 5, 8, 4, 9, 1, 6, 2, 3],
        [1, 3, 4, 7, 8, 9, 2, 5, 6],
        [8, 6, 9, 1, 3, 2, 5, 7, 4],
        [4, 9, 5, 2, 7, 6, 3, 1, 8]];

#
# Copy grid list to another variable
shuff_list = copy.copy(grid);
# Shuffle the list
#shuffle(shuff_list)

# Create a list of indices from 0 to 80 and shuffle them
vals = [x for x in range(1,9*9)]
shuffle(vals)
vals = vals[0:int(len(vals)*0.02)]

num_of_soln = 0;
for ind in range(len(vals)):
    # Define exit condition of solution
    if num_of_soln > 1:
        break;
    # Extract row and col indices from the shuffled 2-d list
    row = vals[ind] % 9;
    col = vals[ind] // 9;   
        
    # Copy the value at the location in case of accidental removal
    hold_val = copy.deepcopy(shuff_list[row][col]);
    temp = copy.deepcopy(shuff_list);
    # Set value of shuffled list position to zero
    temp[row][col] = 0;
    if fill_element(temp, 0, 0):
        shuff_list[row][col] = 0;
        temp = copy.deepcopy(shuff_list);
        continue
    else:
        temp = shuff_list;
        break;
print('\n Print Result')
print_grid(temp)


print('\n Call Sudoku: ')
sudoku(temp)



# 80% of information removed from puzzle
# removed_vals = vals[0:int(len(vals)*0.80)]
# for i in range(len(shuff_list)):
#     shuff_list[][]

    # # Set positions in shuff_list to zero if that position is in removed_vals
    # ind, num_of_soln = 0, 0;
    # while ind < len(vals):
    #     # Define exit condition of solution
    #     if num_of_soln > 1:
    #         break;
    #     # Extract row and col indices from the shuffled 2-d list
    #     row = vals[ind] % 9;
    #     col = vals[ind] // 9;
        
    #     # Copy the value at the location in case of accidental removal
    #     hold_val = copy.copy(shuff_list[row][col]);
    #     # Set value of shuffled list position to zero
    #     shuff_list[row][col] = 0;
        
    #     # Solver checks if the position can be set to zero or not by validating possible solutions
    #     if solver(shuff_list, row, col):
    #         ind += 1; # Increment to next position to be removed
    #         continue
    #     # If the position cannot be set to zero, reset the position in the shuffled list to the held value
    #     shuff_list[row][col] = hold_val;




from sys import argv
import copy

default_sudoku_file = "sudoku.txt"

def brute_force(sudoku, unassigned):
    # TODO : Assign a value to an unassigned cell from its possible value list
    #        Create another sudoku and unassigned dictionary with that value and see if it can be solved
    #        If not, remove that value and go on to the next one till you get the solution

    (x, y), val_list = unassigned.popitem()
    for val in val_list:
        temp_unassigned = copy.deepcopy(unassigned)
        # assign value to temporary sudoku
        sudoku[(x, y)] = val
        # update the temporary unassigned list
        for loc in temp_unassigned:
            in_block = ((loc[0] >= x - (x % 3)) and (loc[0] < x - (x % 3) + 3)) and ((loc[1] >= y - (y % 3)) and (loc[1] < y - (y % 3) + 3))
            if loc[0] == x or loc[1] == y or in_block:
                if val in temp_unassigned[loc]:
                    temp_unassigned[loc].remove(val)
        solved = solve_sudoku(sudoku, temp_unassigned)
        if solved:
            unassigned = temp_unassigned
            return True
        sudoku[(x, y)] = 0
    # if no solution is found
    unassigned[(x, y)] = val_list
    return False


# Tries to solve the sudoku
def solve_sudoku(sudoku, unassigned):
    # check if sudoku is invalid
    if not check_sudoku(sudoku):
        return False
    changed_locations = [] # tracks which locations are changed in the given sudoku
    # loop till all cells are assigned a valid value
    while len(unassigned) > 0:
        # print("-----  UNASSIGNED  -----")
        to_be_removed = [] # list of cell locations to be removed from unassigned dictionary
        for location, val_list in unassigned.items():
            if len(val_list) == 0: # if sudoku can't be solved
                for loc in changed_locations:
                    sudoku[loc] = 0
                return False
            if len(val_list) == 1:
                sudoku[location] = val_list.pop()
                to_be_removed.append(location)
                changed_locations.append(location)
        # if no changes happened
        if len(to_be_removed) == 0:
            solved = brute_force(sudoku, unassigned)
            if not solved: # if sudoku can't be solved
                for loc in changed_locations:
                    sudoku[loc] = 0
            return solved
        # remove the assigned cell locations
        for location in to_be_removed:
            unassigned.pop(location)
        # update the unassigned dictionary
        for location, val_list in unassigned.items():
            for val in val_list:
                if check_block(location[0], location[1], sudoku, val) and check_row_clmn(location[0], location[1], sudoku, val):
                    continue
                val_list.remove(val)
        if not check_sudoku(sudoku):
            for loc in changed_locations:
                sudoku[loc] = 0
            return False
    if not check_sudoku(sudoku):
        print("Solution Incorrect :(")
    return True


# checks if the value is repeated within its block
def check_block(x, y, sudoku, val = None):
    if val is None: # no value argument given
        val = sudoku[(x, y)]
    if val == 0: # if no value assigned yet
        return True
    # iterate through the block
    for i in range(x - (x % 3), x - (x % 3) + 3):
        for j in range(y - (y % 3), y - (y % 3) + 3):
            if i == x and j == y: # skip the input location
                continue
            if sudoku[(i, j)] == val:
                return False
    return True


# checks if the value is repeated in its row or coloumn
def check_row_clmn(x, y, sudoku, val = None):
    if val is None: # no value argument given
        val = sudoku[(x, y)]
    if val == 0: # if no value assigned yet
        return True
    # iterate through the coloumn
    for i in range(9):
        if i == x: # skip the input location
            continue
        if sudoku[(i, y)] == val:
            return False
    # iterate through the row
    for j in range(9):
        if j == y: # skip the input location
            continue
        if sudoku[(x, j)] == val:
            return False
    return True


# checks if the sudoku is illegal
def check_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[(i, j)] == 0: # if no value assigned yet
                continue
            if check_block(i, j, sudoku) and check_row_clmn(i, j, sudoku):
                continue
            return False
    return True


# prints the given sudoku dictionary
def print_sudoku(sudoku):
    print()
    for i in range(9):
        for j in range(9):
            if sudoku[(i, j)] == 0:
                print('_', end='')
            else:
                print(sudoku[(i, j)], end='')
            
            if j == 8:
                print()
            elif j % 3 == 2:
                print(" | ", end='')
            else:
                print(' ', end='')
        if i == 8:
            print()
        elif i % 3 == 2:
            print('---------------------')


# returns a list of possible values for the given unassigned location
def get_possible_vals(x, y, sudoku):
    temp = []
    for val in range(1, 10):
        if check_block(x, y, sudoku, val) and check_row_clmn(x, y, sudoku, val):
            temp.append(val)
    return temp


# gets the sudoku to be solved
def get_sudoku():
    # check command line arguments
    if len(argv) != 2:
        sudoku_file = default_sudoku_file
    else:
        sudoku_file = argv[1]
        
    sudoku = {}
    unassigned = {} # list of unassigned location tuples
    # Open csv file
    with open(sudoku_file) as file:
        i, j = 0, 0 # row and coloumn indices
        for line in file: # read a line
            if line[0] == '-': # skip if partition line
                continue
            row = ' '.join(line.strip().split(' | ')).split() # create a list of values in line
            # update values in sudoku dictionary
            for c in row:
                if c == '_':
                    sudoku[(i, j)] = 0
                    unassigned[(i, j)] = None
                else:
                    sudoku[(i, j)] = int(c)
                j += 1
            i += 1
            j = 0
    
    for x, y in unassigned:
        unassigned[(x, y)] = get_possible_vals(x, y, sudoku)

    return sudoku, unassigned
    

if __name__ == "__main__":
    print("\nFetching Sudoku ...")
    sudoku, unassigned = get_sudoku()
    print("Sudoku Fetched!")
    
    print_sudoku(sudoku)

    print("Solving ...")
    solved = solve_sudoku(sudoku, unassigned)

    if solved:
        print()
        print("SOLVED!!")
    else:
        print("Invalid Sudoku (¬_¬)")
    
    print_sudoku(sudoku)
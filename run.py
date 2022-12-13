

# Board for holding ship locations
HIDDEN_BOARD = [[''] * 8 for x in range(8)]
# Board for displaying hits and miss
GUESS_BOARD = [[''] * 8 for x in range(8)]

let_to_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

# Define Function to Print Battleship Board
def print_board(board):
    print(' A B C D E F G H')
    print(' ---------------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# Define Function to create the ships
def create_ships(board):
    pass


# Define Function to get ship location
def get_ship_location():
    pass


# Define Function to count hit ships
def count_hit_ships():
    pass

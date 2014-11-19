class IllegalMove(EnvironmentError):
    pass

def build_grid():
    return [[' ', ' ', ' '], 
            [' ', ' ', ' '], 
            [' ', ' ', ' ']]

def play(grid, player, col, row):
    if (col > 2 or row > 2):
        raise IllegalMove("dupa", col, row)
    
    grid[row][col] = player
    
def get_winner(grid):
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']
    
    for i in range(3):
        if (grid[i] == x_win or get_col(grid, i) == x_win):
            return 'X'
        if (grid[i] == o_win or get_col(grid, i) == o_win):
            return 'O'
        
    if (get_diag(grid, 1) == x_win or get_diag(grid, 2) == x_win):
        return 'X'
    if (get_diag(grid, 1) == o_win or get_diag(grid, 2) == o_win):
        return 'O'
    
    return 'NONE'

def get_col(grid, col):
    return [grid[0][col], grid[1][col], grid[2][col]]

def get_diag(grid, diag):
    if (diag == 1):
        return [grid[0][0], grid[1][1], grid[2][2]]
    else:
        return [grid[0][-1], grid[1][-2], grid[2][-3]]

grid = build_grid()
play(grid, 'X', 1, 1)
play(grid, 'X', 0, 0)
play(grid, 'X', 2, 2)
play(grid, 'O', 2, 0)
play(grid, 'O', 2, 1)
play(grid, 'O', 2, 2)

try:
    play(grid, 'X', 3, 3)
except (IllegalMove), e:
    print str(e)
    print e.errno
finally:
    print 'finally'

print get_winner(grid)
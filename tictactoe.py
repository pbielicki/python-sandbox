def build_grid():
    return [3 * [' '] for _i in range(3)]

def play(grid, player, col, row):
    if grid[row][col] == ' ':
        grid[row][col] = player
    
def get_winner(grid):
    winner = [('X', 3 * ['X']), ('O', 3 * ['O'])]
    
    for i in range(3):
        for (player, v) in winner:
            if (grid[i] == v or get_col(grid, i) == v or get_diag(grid, i) == v):
                return player
        
    return 'NONE'

def get_row(grid, row):
    return grid[row]

def get_col(grid, col):
    #return [grid[0][col], grid[1][col], grid[2][col]]
    return [row[col] for row in grid]

def get_diag(grid, diag):
    if (diag == 1):
        return [grid[0][0], grid[1][1], grid[2][2]]

    return [grid[0][-1], grid[1][-2], grid[2][-3]]

grid = build_grid()
play(grid, 'X', 1, 1)
play(grid, 'X', 0, 0)
#play(grid, 'X', 2, 2)
play(grid, 'O', 2, 0)
play(grid, 'O', 2, 1)
#play(grid, 'O', 2, 2)

print get_winner(grid)
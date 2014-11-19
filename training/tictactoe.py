"""
Tic Tac Toe

The grid is a list of 3 lists of 3 strings.
The possible values are:

* ' ' for an empty position,
* 'O' for a mark of player O
* 'X' for a mark of player X
"""

class IllegalMove(Exception):
    '''signal a wrong move
    (wrong col/row num, already played move...)
    '''
    pass

def build_grid():
    """return an empty grid"""
    grid = [3* [' '] for i in range(3)] 
    return grid

def play(grid, player, rownum, colnum):
    """put player mark at (rownum,colnum) if the space is free

    this function modifies the grid (and does not return anything)
    """
    if not (0 <= rownum < 3):
        raise IllegalMove('wrong row number', rownum)
    if not (0 <= colnum < 3):
        raise IllegalMove('wrong column number', colnum)
    if player not in 'XO':
        raise IllegalMove('unknown player4m player', player)
    
    if grid[rownum][colnum] == ' ':
        grid[rownum][colnum] = player
    else:
        raise IllegalMove('space already played', rownum, colnum)

def get_row(grid, rownum):
    """return the row rownum as a list of 3 strings"""
    return grid[rownum]

def get_col(grid, colnum):
    """return the col colnum as a list of 3 strings"""
    col = []
    for row in grid:
        col.append(row[colnum])
    return col
    # or
    # return [row[colnum] for row in grid]

def get_diag(grid, diagnum):
    """return the diagonal diagnum as a list of 3 strings"""
    diag = []
    if diagnum == 1:
        grid = list(reversed(grid))
    for i in xrange(3):
        diag.append(grid[i][i])
    return diag
    
def is_winning(plays):
    '''return True if this has 3 marks'''
    for player in 'XO':
        if plays == [player] *3:
            return True
    return False
    

def get_winner(grid): # nicer version found below
    """return 'X' or 'O' if the corresponding player has won, and ' ' otherwise"""
    for i in xrange(3):
        candidate = get_row(grid, i)
        if is_winning(candidate):
            return candidate[0]
        candidate = get_col(grid, i)
        if is_winning(candidate):
            return candidate[0]
    for i in xrange(2):
        candidate = get_diag(grid)
        if is_winning(candidate):
            return candidate[0]
    return ' '        

def get_winner(grid):
    """return 'X' or 'O' if the corresponding player has won, and ' ' otherwise"""
    extractors = [(get_row, 3),
                  (get_col, 3),
                  (get_diag, 2),
                  ]
    for extractor, max_range in extractors:
        for i in range(max_range):
            candidate = extractor(grid, i)
            if is_winning(candidate):   
                return candidate[0]
    return ' '        


def test():
    grid = build_grid()
    print grid
    play(grid, 'X', 0, 0)
    print grid
    print get_winner(grid)
    play(grid, 'O', 1, 0)
    print get_winner(grid)
    play(grid, 'X', 0, 1)
    print get_winner(grid)
    play(grid, 'O', 2, 0)
    print get_winner(grid)
    play(grid, 'X', 0, 2)
    print get_winner(grid)
    try:
        play(grid, 'X', 0, 5)
    except IllegalMove, exc:
        print exc
    
print __name__
if __name__ == '__main__':
    test()

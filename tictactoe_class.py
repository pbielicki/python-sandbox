class Grid(object):
    def __init__(self):
        self.grid = [3 * ['_'] for _i in range(3)]
        
    def play(self, player, row, col):
        if row < 3 and col < 3 and self.grid[row][col] == '_':
                self.grid[row][col] = player
             
    def get_winner(self):
        winner = [('X', 3 * ['X']), ('O', 3 * ['O'])]
        
        for i in range(3):
            for (player, v) in winner:
                if (self._get_row(i) == v or self._get_col(i) == v or self._get_diag(i) == v):
                    return player
             
    def _get_row(self, row):
        return self.grid[row]    
        
    def _get_col(self, col):
        return [self.grid[i][col] for i in range(3)]

    def _get_diag(self, diag):
        if (diag == 1):
            return [self.grid[i][i] for i in range(3)]
    
        return [self.grid[i][-1 - i] for i in range(3)]
    
    def __str__(self):
        s = ''
        for row in range(3):
            for col in range(3):
                s += self.grid[row][col] + ' '
            
            s += '\n'
        return s[:-1]
        
grid = Grid()
print grid
grid.play('X', 1, 1)
grid.play('X', 0, 0)
#grid.play('X', 2, 2)
grid.play('O', 2, 0)
grid.play('O', 2, 1)
grid.play('O', 2, 2)
print grid

print 'the winner is', grid.get_winner()
    
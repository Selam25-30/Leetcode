from typing import List

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.position_map = {}
        
        # Populate position_map with (value: (row, col)) for quick lookup
        for i in range(self.n):
            for j in range(self.n):
                self.position_map[grid[i][j]] = (i, j)
    
    def adjacentSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        i, j = self.position_map[value]
        sum_adjacent = 0
        
        # Check all four possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                sum_adjacent += self.grid[ni][nj]
        
        return sum_adjacent
    
    def diagonalSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        i, j = self.position_map[value]
        sum_diagonal = 0
        
        # Check all four possible diagonal directions
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for di, dj in diagonals:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                sum_diagonal += self.grid[ni][nj]
        
        return sum_diagonal

 # Your NeighborSum object will be instantiated and called as such:
# # obj = NeighborSum(grid)
# # param_1 = obj.adjacentSum(value)
# # param_2 = obj.diagonalSum(value)
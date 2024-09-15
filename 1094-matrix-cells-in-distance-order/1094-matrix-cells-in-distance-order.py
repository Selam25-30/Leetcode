class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Step 1: Create a list of all coordinates
        cells = [(r, c) for r in range(rows) for c in range(cols)]
        
        # Step 2: Sort the cells based on the Manhattan distance from (rCenter, cCenter)
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        # Step 3: Return the sorted list of coordinates
        return cells

from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Initial position at the top-left corner
        row, col = 0, 0
        
        # Process each command to move the snake
        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            elif command == "RIGHT":
                col += 1
        
        # Calculate the final position in the linear array
        return row * n + col

# Example usage:
# sol = Solution()
# print(sol.finalPositionOfSnake(2, ["RIGHT","DOWN"]))  # Output: 3
# print(sol.finalPositionOfSnake(3, ["DOWN","RIGHT","UP"]))  # Output: 1

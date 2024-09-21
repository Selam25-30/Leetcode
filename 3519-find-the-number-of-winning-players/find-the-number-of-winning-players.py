from collections import defaultdict
from typing import List

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Dictionary to keep track of how many balls of each color each player picked
        ball_count = defaultdict(lambda: defaultdict(int))
        
        # Count the number of balls each player picks of each color
        for player, color in pick:
            ball_count[player][color] += 1
        
        winners = 0
        
        # Check for each player if they win
        for player in range(n):
            # Find the maximum number of balls of the same color the player picked
            max_balls_of_same_color = max(ball_count[player].values(), default=0)
            
            # Player wins if they picked at least player + 1 balls of the same color
            if max_balls_of_same_color >= player + 1:
                winners += 1
        
        return winners

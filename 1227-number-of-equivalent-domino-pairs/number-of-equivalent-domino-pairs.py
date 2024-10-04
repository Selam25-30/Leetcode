from typing import List
from collections import defaultdict

class Solution: 
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        
        # Normalize and count each domino
        for a, b in dominoes:
            normalized = tuple(sorted((a, b)))
            count[normalized] += 1
        
        # Calculate the number of pairs for each unique domino
        result = 0
        for num in count.values():
            if num > 1:
                result += (num * (num - 1)) // 2  # Combination of pairs (n choose 2)
        
        return result

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize with the first array's minimum and maximum
        current_min = arrays[0][0]
        current_max = arrays[0][-1]
        max_distance = 0
        
        # Iterate over the remaining arrays
        for i in range(1, len(arrays)):
            # Calculate possible distances
            max_distance = max(max_distance, abs(arrays[i][-1] - current_min))
            max_distance = max(max_distance, abs(current_max - arrays[i][0]))
            
            # Update current_min and current_max
            current_min = min(current_min, arrays[i][0])
            current_max = max(current_max, arrays[i][-1])
        
        return max_distance

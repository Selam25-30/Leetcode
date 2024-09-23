from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # To track how many flowers we can plant
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current plot is empty (flowerbed[i] == 0)
            # Also check the left plot (flowerbed[i-1] == 0 or i == 0) and right plot (flowerbed[i+1] == 0 or i == length - 1)
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                # Plant a flower at the current plot
                flowerbed[i] = 1
                count += 1
                
                # If we already planted enough flowers, return True
                if count >= n:
                    return True
        
        # After the loop, check if we were able to plant all required flowers
        return count >= n

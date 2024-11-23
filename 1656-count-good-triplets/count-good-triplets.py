from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)

        # Iterate through all possible triplets (i, j, k)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:  # First condition
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:  # Second and third conditions
                            count += 1
        
        return count

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = missing = -1
        
        # Identify duplicate and missing number
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        # Find the missing number
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        
        return [duplicate, missing]

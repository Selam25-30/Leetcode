from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        # The maximum product will come from the two largest numbers
        return (nums[0] - 1) * (nums[1] - 1)

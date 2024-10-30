from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sort the array to easily get the two smallest and two largest values
        nums.sort()
        # Calculate the product difference
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set and compare its length with the original list
        return len(nums) != len(set(nums))

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark the numbers that appear in the array
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        
        # Collect the numbers that didn't appear
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result

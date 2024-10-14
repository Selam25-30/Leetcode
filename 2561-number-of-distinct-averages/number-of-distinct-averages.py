class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Sort the nums array
        nums.sort()
        
        # Initialize a set to keep track of distinct averages
        distinct_averages = set()
        
        # Use two pointers: one from the start and one from the end
        left = 0
        right = len(nums) - 1
        
        # Loop until all elements are processed
        while left < right:
            # Calculate the average of the current minimum and maximum
            avg = (nums[left] + nums[right]) / 2
            # Add the average to the set
            distinct_averages.add(avg)
            # Move pointers inward
            left += 1
            right -= 1
        
        # Return the number of distinct averages
        return len(distinct_averages)

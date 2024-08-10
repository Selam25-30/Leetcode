from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array first
        nums.sort()
        closest_sum = float('inf')  # Initialize with an infinitely large value
        
        # Traverse through each element in the array
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Set the two pointers
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is closer to the target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison of current_sum and target
                if current_sum < target:
                    left += 1  # Increase the sum by moving the left pointer to the right
                elif current_sum > target:
                    right -= 1  # Decrease the sum by moving the right pointer to the left
                else:
                    # If the current_sum is exactly equal to the target, return it immediately
                    return current_sum
        
        return closest_sum

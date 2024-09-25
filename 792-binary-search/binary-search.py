from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # To prevent overflow in other languages
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        
        return -1  # Target not found

# Example usage:
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
print(solution.search([-1, 0, 3, 5, 9, 12], 2))  # Output: -1

class Solution:
    def sum_of_digits(self, n: int) -> int:
        # This helper function returns the sum of digits of a number n
        return sum(int(digit) for digit in str(n))
    
    def minElement(self, nums: List[int]) -> int:
        # Replace each element in nums with the sum of its digits
        replaced_nums = [self.sum_of_digits(num) for num in nums]
        # Return the minimum element from the replaced numbers
        return min(replaced_nums)

# Example usage:
sol = Solution()

# Example 1
nums1 = [10, 12, 13, 14]
print(sol.minElement(nums1))  # Output: 1

# Example 2
nums2 = [1, 2, 3, 4]
print(sol.minElement(nums2))  # Output: 1

# Example 3
nums3 = [999, 19, 199]
print(sol.minElement(nums3))  # Output: 10

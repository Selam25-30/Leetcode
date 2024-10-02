from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the numbers
        nums.sort()
        # Take the sum of every other element (since sorted pairs' smaller elements contribute more)
        return sum(nums[::2])

# Test with the provided example cases
solution = Solution()
test_case_1 = [1, 4, 3, 2]
test_case_2 = [6, 2, 6, 5, 1, 2]

output_1 = solution.arrayPairSum(test_case_1)
output_2 = solution.arrayPairSum(test_case_2)

output_1, output_2
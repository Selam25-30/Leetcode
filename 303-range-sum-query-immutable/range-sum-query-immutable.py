class NumArray:

    def __init__(self, nums: List[int]):
        # Create a prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            # prefix_sum[i + 1] holds the sum of nums[0] to nums[i]
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum in range [left, right] using the prefix sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

numArray = NumArray([-2, 0, 3, -5, 2, -1])


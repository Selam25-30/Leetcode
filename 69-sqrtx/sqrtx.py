class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

# Example usage:
sol = Solution()
print(sol.mySqrt(4))  # Output: 2
print(sol.mySqrt(8))  # Output: 2

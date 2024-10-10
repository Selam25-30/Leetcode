class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # For even n, add pairs of integers (i, -i)
        # For odd n, also include a 0
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        # If n is odd, include 0 to make the sum zero
        if n % 2 == 1:
            result.append(0)
        
        return result

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            # If no operations are given, the whole matrix is filled with 0s
            return m * n
        
        # Find the minimum ai and bi from ops
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        
        # The number of maximum integers will be the area of the smallest affected sub-matrix
        return min_a * min_b

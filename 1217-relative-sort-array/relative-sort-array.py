from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the order of elements in arr2
        order = {num: i for i, num in enumerate(arr2)}
        
        # Sort arr1 using a custom sorting key
        # Elements in arr2 are sorted by their order in arr2, others are sorted by value
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))

# Example usage:
solution = Solution()
print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
# Output: [2,2,2,1,4,3,3,9,6,7,19]

print(solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
# Output: [22,28,8,6,17,44]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # Count the zeros in the original array
        zeros = arr.count(0)
        
        # Traverse the array from the end to the beginning
        for i in range(n - 1, -1, -1):
            # If the index plus the number of zeros to its right is still within the array bounds
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            
            # If the current element is zero, we need to "duplicate" it
            if arr[i] == 0:
                zeros -= 1
                # Place the duplicated zero if within the bounds
                if i + zeros < n:
                    arr[i + zeros] = 0

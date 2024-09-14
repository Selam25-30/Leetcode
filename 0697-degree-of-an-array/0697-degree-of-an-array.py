class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Step 1: Dictionary to store the frequency, first, and last occurrence of each number
        frequency = {}
        first_occurrence = {}
        last_occurrence = {}
        
        # Step 2: Traverse through the list and fill frequency, first_occurrence, and last_occurrence
        for i, num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 0
                first_occurrence[num] = i
            frequency[num] += 1
            last_occurrence[num] = i
        
        # Step 3: Find the degree of the array (maximum frequency)
        degree = max(frequency.values())
        
        # Step 4: Find the minimum length of the subarray for elements with frequency == degree
        min_length = len(nums)
        for num in frequency:
            if frequency[num] == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
        
        return min_length

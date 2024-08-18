class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        
        # Sort the nums array to easily find min and max elements
        nums.sort()
        
        while nums:
            # Remove the smallest and largest elements
            minElement = nums.pop(0)
            maxElement = nums.pop(-1)
            
            # Add the average of these two elements to averages
            averages.append((minElement + maxElement) / 2)
        
        # Return the minimum element in averages
        return min(averages)

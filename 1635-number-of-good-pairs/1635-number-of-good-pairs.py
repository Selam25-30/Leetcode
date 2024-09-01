class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        good_pairs = 0
        
        # Count the frequency of each number in the array
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Calculate the number of good pairs
        for key in count:
            n = count[key]
            if n > 1:
                good_pairs += n * (n - 1) // 2
                
        return good_pairs

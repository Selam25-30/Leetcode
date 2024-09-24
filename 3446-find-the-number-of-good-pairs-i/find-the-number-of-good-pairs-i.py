class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0  # to store the number of good pairs
        
        # Iterate over all pairs of indices (i, j)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # Check if nums1[i] is divisible by nums2[j] * k
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
                    
        return count

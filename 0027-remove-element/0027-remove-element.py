class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Pointer to track the position of non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to position k
                k += 1  # Increment k to move to the next position

        return k
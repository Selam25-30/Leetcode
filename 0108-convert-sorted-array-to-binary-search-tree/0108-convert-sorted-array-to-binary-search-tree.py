# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the array is empty, return None
        if not nums:
            return None
        
        # Find the middle index
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively build the left subtree using the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively build the right subtree using the right half of the array
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

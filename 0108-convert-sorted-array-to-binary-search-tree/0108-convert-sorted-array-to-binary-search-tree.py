# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def buildBST(left, right):
            if left > right:
                return None
            
            # Choose the middle element to ensure balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively construct left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, len(nums) - 1)
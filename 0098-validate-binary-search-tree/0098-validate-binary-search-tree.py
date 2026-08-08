# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            if not node:
                return True
            
            # The current node value must be strictly within the range (low, high)
            if not (low < node.val < high):
                return False
            
            # Left subtree values must be strictly less than node.val
            # Right subtree values must be strictly greater than node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))
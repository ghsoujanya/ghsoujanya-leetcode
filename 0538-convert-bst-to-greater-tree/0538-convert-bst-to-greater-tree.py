# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.total = 0
        
        def reverse_in_order(node):
            if not node:
                return
            
            # 1. Visit right subtree first (larger values)
            reverse_in_order(node.right)
            
            # 2. Process current node
            self.total += node.val
            node.val = self.total
            
            # 3. Visit left subtree (smaller values)
            reverse_in_order(node.left)
            
        reverse_in_order(root)
        return root
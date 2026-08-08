# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        curr = root
        
        while curr:
            if curr.left is None:
                # Process current node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find predecessor in left subtree
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if pred.right is None:
                    # Create temporary link back to current
                    pred.right = curr
                    curr = curr.left
                else:
                    # Break temporary link and process current node
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
        
        # Swap the values of the two mismatched nodes
        if first and second:
            first.val, second.val = second.val, first.val
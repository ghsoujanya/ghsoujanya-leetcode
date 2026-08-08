# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map values to their indices in inorder traversal for O(1) lookups
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            # If there are no elements to construct the subtree
            if in_left > in_right:
                return None
            
            # Pick current postorder element as the root
            val = postorder.pop()
            root = TreeNode(val)
            
            # Root splits inorder array into left and right subtrees
            index = inorder_index_map[val]
            
            # Build right subtree first because postorder pops from the end
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root

        return helper(0, len(inorder) - 1)
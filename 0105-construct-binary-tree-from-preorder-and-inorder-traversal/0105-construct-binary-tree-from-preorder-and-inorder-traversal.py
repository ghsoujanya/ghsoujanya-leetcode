# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map values to their indices in the inorder traversal for O(1) lookups
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to keep track of the current root in preorder array
        self.pre_idx = 0
        
        def array_to_tree(left, right):
            # Base case: no elements to construct the subtree
            if left > right:
                return None
            
            # Select the current root value from preorder and increment pointer
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Index of current root in inorder array
            in_idx = inorder_index_map[root_val]
            
            # Build left and right subtrees
            # Note: Left subtree must be built first because preorder is (Root -> Left -> Right)
            root.left = array_to_tree(left, in_idx - 1)
            root.right = array_to_tree(in_idx + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)
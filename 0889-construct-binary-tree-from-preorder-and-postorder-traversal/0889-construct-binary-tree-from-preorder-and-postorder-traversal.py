# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not postorder:
            return None
        
        # The first element of preorder is the root
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # The second element of preorder is the root of the left subtree
        left_root_val = preorder[1]
        
        # Find how many nodes are in the left subtree by finding left_root_val in postorder
        left_subtree_size = postorder.index(left_root_val) + 1
        
        # Recursively construct left and right subtrees
        root.left = self.constructFromPrePost(
            preorder[1 : 1 + left_subtree_size], 
            postorder[:left_subtree_size]
        )
        root.right = self.constructFromPrePost(
            preorder[1 + left_subtree_size :], 
            postorder[left_subtree_size : -1]
        )
        
        return root
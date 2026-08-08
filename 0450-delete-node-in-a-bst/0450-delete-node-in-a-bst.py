# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # Search for the node in the left or right subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            # Case 1 & 2: Node with zero or one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 3: Node with two children
            # Find the minimum node in the right subtree (in-order successor)
            curr = root.right
            while curr.left:
                curr = curr.left

            # Copy the successor's value to this node
            root.val = curr.val

            # Delete the in-order successor from the right subtree
            root.right = self.deleteNode(root.right, curr.val)

        return root
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
            
        # Queue storing tuples of (node, parent_node)
        queue = deque([(root, None)])
        
        while queue:
            level_size = len(queue)
            x_parent = None
            y_parent = None
            
            for _ in range(level_size):
                node, parent = queue.popleft()
                
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # If both nodes were found at the current level
            if x_parent or y_parent:
                return x_parent is not None and y_parent is not None and x_parent != y_parent
                
        return False
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_all_left(root)

    def _push_all_left(self, node):
        """Helper to push all left descendants of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        # The top element on the stack is the smallest element remaining
        top_node = self.stack.pop()
        
        # If the node has a right child, push all its left descendants
        if top_node.right:
            self._push_all_left(top_node.right)
            
        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
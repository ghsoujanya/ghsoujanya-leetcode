from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []
        
        nodes_by_col = defaultdict(list)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            nodes_by_col[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        res = []
        for col in sorted(nodes_by_col.keys()):
            nodes_by_col[col].sort(key=lambda x: (x[0], x[1]))
            res.append([val for row, val in nodes_by_col[col]])
            
        return res
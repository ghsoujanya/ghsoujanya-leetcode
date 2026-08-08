from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root or not target:
            return []
        
        # Step 1: Build parent map using BFS
        parent_map = {}
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            if curr.left:
                parent_map[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent_map[curr.right] = curr
                queue.append(curr.right)
                
        # Step 2: BFS starting from target to find nodes at distance K
        visited = {target}
        queue = deque([target])
        current_distance = 0
        
        while queue:
            if current_distance == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                # Check left child, right child, and parent
                neighbors = [curr.left, curr.right, parent_map.get(curr)]
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            current_distance += 1
            
        return []
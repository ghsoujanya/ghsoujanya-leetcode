from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 0: uncolored, 1: color A, -1: color B
        color = [0] * n
        
        for i in range(n):
            # Skip if node is already colored
            if color[i] != 0:
                continue
            
            # Start BFS for the current connected component
            queue = deque([i])
            color[i] = 1  # Assign initial color
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        # Color neighbor with the opposite color
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Conflict detected: adjacent nodes have the same color
                        return False
                        
        return True
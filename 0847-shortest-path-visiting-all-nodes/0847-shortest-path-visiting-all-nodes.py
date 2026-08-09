from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        
        # Target mask where all n bits are set to 1
        target_mask = (1 << n) - 1
        
        # Queue stores tuples of (current_node, current_mask)
        queue = deque()
        
        # visited array/set to keep track of (node, mask)
        visited = set()
        
        # Initialize BFS with all nodes as starting candidates
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask))
            visited.add((i, mask))
            
        steps = 0
        
        while queue:
            # Process level by level to track the number of steps/edges
            for _ in range(len(queue)):
                curr_node, curr_mask = queue.popleft()
                
                # If all nodes have been visited
                if curr_mask == target_mask:
                    return steps
                
                # Explore neighbors
                for neighbor in graph[curr_node]:
                    next_mask = curr_mask | (1 << neighbor)
                    if (neighbor, next_mask) not in visited:
                        visited.add((neighbor, next_mask))
                        queue.append((neighbor, next_mask))
            
            steps += 1
            
        return steps
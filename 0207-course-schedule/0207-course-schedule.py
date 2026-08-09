from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build adjacency list and in-degree array
        # [a, b] means b -> a (b is a prerequisite for a)
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # Queue all nodes with in-degree 0 (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed_courses = 0
        
        while queue:
            curr = queue.popleft()
            processed_courses += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return processed_courses == numCourses
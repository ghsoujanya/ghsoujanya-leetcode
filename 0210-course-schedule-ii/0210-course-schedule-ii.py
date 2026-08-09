from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build graph and in-degree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Add nodes with 0 in-degree to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Process nodes
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Return ordering if all courses were processed; otherwise return []
        return order if len(order) == numCourses else []
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        complete_count = 0
        
        for i in range(n):
            if i not in visited:
                component = []
                # Traverse the connected component using DFS/BFS
                stack = [i]
                visited.add(i)
                
                while stack:
                    curr = stack.pop()
                    component.append(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                
                # Check completeness condition:
                # Every node in a complete component of size v must have a degree of v - 1.
                v = len(component)
                is_complete = all(len(graph[node]) == v - 1 for node in component)
                
                if is_complete:
                    complete_count += 1
                    
        return complete_count
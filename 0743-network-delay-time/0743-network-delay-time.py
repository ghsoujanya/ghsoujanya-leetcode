import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list: node -> list of (neighbor, weight)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Min-heap stores tuples of (current_time, node)
        min_heap = [(0, k)]
        # Map to store shortest distance to each node
        distances = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in distances:
                continue
            
            distances[node] = time
            
            # If all nodes visited, early stop
            if len(distances) == n:
                return time
            
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        # If we couldn't reach all nodes
        return max(distances.values()) if len(distances) == n else -1
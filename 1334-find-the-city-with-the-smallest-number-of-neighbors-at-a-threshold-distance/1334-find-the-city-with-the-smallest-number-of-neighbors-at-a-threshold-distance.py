class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            
        # Step 2: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # Step 3: Find the city with the minimum reachable cities within threshold
        min_reachable = float('inf')
        result_city = -1
        
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            # Tie-breaker: If counts are equal, prefer the larger city index
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                result_city = i
                
        return result_city
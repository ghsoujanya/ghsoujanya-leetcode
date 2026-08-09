import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Min-heap stores tuples of (time, r, c)
        min_heap = [(grid[0][0], 0, 0)]
        
        visited = set()
        visited.add((0, 0))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            
            # Reached the bottom-right corner
            if r == n - 1 and c == n - 1:
                return t
            
            # Explore 4-directional neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # The required time to reach (nr, nc) is max(current_time, grid[nr][nc])
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))

        return -1
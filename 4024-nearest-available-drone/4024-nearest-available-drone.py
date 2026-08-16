class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        best_idx = -1
        min_dist = float('inf')
        
        for i, (x, y, r) in enumerate(drones):
            dist = abs(x - tx) + abs(y - ty)
            # Check if reachable and strictly closer than previous candidate
            if dist <= r and dist < min_dist:
                min_dist = dist
                best_idx = i
                
        return best_idx
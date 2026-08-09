class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] stores the minimum cost to reach column j in the current row
        dp = grid[0][:]
        
        for r in range(1, m):
            next_dp = [float('inf')] * n
            for col in range(n):
                cell_val = grid[r][col]
                for prev_col in range(n):
                    val = grid[r - 1][prev_col]
                    cost = dp[prev_col] + moveCost[val][col] + cell_val
                    if cost < next_dp[col]:
                        next_dp[col] = cost
            dp = next_dp
            
        return min(dp)
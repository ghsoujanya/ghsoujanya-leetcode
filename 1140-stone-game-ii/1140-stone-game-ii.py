from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            # If the current player can take all remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2 * m
            for x in range(1, 2 * m + 1):
                # Stones obtained = Total remaining stones - best opponent response
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, max(m, x)))
                
            return max_stones
            
        return dp(0, 1)
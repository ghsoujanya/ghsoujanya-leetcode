from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Compute prefix sums of the array
        prefix_sums = list(accumulate(stones))
        
        # Base case: taking all stones gives prefix_sums[-1]
        # At index n - 2, the player must take all stones (up to index n - 1)
        ans = prefix_sums[-1]
        
        # Iterate backwards from index n - 2 down to index 1
        # (Since x > 1, Alice must pick at least 2 stones, so index >= 1)
        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, prefix_sums[i] - ans)
            
        return ans
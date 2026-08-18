from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: k == n -> Entire array is the only subarray
        if k == n:
            return max(nums)
        
        # Case 2: k == 1 -> Find largest element appearing exactly once in the array
        if k == 1:
            unique_elements = [x for x, freq in counts.items() if freq == 1]
            return max(unique_elements) if unique_elements else -1
        
        # Case 3: 1 < k < n -> Only first or last elements can belong to exactly 1 subarray
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
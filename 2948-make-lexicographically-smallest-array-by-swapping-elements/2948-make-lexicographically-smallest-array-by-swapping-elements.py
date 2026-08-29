from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each value with its original index and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        
        # Group connected components
        i = 0
        while i < n:
            j = i
            # Find the boundary of the current connected component
            while j + 1 < n and sorted_nums[j + 1][0] - sorted_nums[j][0] <= limit:
                j += 1
            
            # Extract indices for this component and sort them
            indices = sorted(sorted_nums[k][1] for k in range(i, j + 1))
            
            # Reassign values to original positions in sorted order
            for k in range(i, j + 1):
                val = sorted_nums[k][0]
                idx = indices[k - i]
                result[idx] = val
                
            i = j + 1
            
        return result
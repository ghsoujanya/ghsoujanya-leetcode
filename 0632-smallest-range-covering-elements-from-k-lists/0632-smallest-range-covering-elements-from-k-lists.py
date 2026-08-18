import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        
        # Initialize heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
            
        range_start, range_end = float('-inf'), float('inf')
        
        while len(min_heap) == len(nums):
            min_val, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Update best range if current window is smaller
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val
                
            # Advance pointer in the list that contained min_val
            if elem_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
                max_val = max(max_val, next_val)
                
        return [range_start, range_end]
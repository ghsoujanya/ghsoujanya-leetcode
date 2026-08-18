import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or k == 0:
            return res
        
        min_heap = []
        
        # Initialize heap with (sum, i, j) where j = 0 for up to k elements of nums1
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        while min_heap and len(res) < k:
            val, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2, push it into the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res
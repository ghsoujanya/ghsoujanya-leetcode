import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push the head of each non-empty list into the heap
        for i, head in enumerate(lists):
            if head:
                # Include list index i to prevent comparison between ListNode instances
                heapq.heappush(min_heap, (head.val, i, head))
                
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next node, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
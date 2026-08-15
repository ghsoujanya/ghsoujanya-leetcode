from functools import reduce
import operator

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Check if all elements are zero
        if all(x == 0 for x in nums):
            return 0
        
        # Calculate the XOR sum of all elements
        total_xor = reduce(operator.xor, nums, 0)
        
        # If total XOR is already non-zero, take the full array
        # Otherwise, drop one element to make it non-zero
        return len(nums) if total_xor != 0 else len(nums) - 1
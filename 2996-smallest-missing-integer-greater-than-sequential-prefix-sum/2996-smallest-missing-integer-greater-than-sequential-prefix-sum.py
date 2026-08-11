class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Find the sum of the longest sequential prefix starting at index 0
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break
        
        # Step 2: Store elements in a set for O(1) lookup
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer x >= s
        while s in num_set:
            s += 1
            
        return s
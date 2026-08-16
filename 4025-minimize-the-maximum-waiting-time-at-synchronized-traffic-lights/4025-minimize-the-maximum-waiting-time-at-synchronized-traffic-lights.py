class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        max_light = max(lights)
        
        # Calculate r = arrivalTime % period for all cars
        remainders = [t % period for t in arrivalTime]
        
        def can_achieve(W: int) -> bool:
            # Maximum light threshold required for cars where r < period - W
            req = 0
            limit = period - W
            for r in remainders:
                if r < limit:
                    req = max(req, r + 1)
            return max_light >= req

        left, right = 0, period - 1
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
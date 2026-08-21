import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Step 1: Filter out redundant coins
        coins.sort()
        filtered_coins = []
        for coin in coins:
            if not any(coin % c == 0 for c in filtered_coins):
                filtered_coins.append(coin)
        
        # Precompute LCMs and subset sizes to speed up PIE
        subsets = []
        n = len(filtered_coins)
        for r in range(1, n + 1):
            for combo in combinations(filtered_coins, r):
                lcm_val = combo[0]
                for coin in combo[1:]:
                    lcm_val = (lcm_val * coin) // math.gcd(lcm_val, coin)
                # Store (lcm_val, sign) -> +1 for odd subset size, -1 for even
                sign = 1 if r % 2 == 1 else -1
                subsets.append((lcm_val, sign))
        
        # Helper function: count unique amounts <= target
        def count_amounts(target: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (target // lcm_val)
            return total

        # Step 2: Binary Search for the K-th smallest amount
        low = filtered_coins[0]
        high = k * filtered_coins[0]
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1

        return ans
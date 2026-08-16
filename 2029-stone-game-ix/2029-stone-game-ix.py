class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Count remainders modulo 3
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1

        # If count of 0-remainder stones is even
        if cnt[0] % 2 == 0:
            return min(cnt[1], cnt[2]) >= 1

        # If count of 0-remainder stones is odd
        return abs(cnt[1] - cnt[2]) > 2
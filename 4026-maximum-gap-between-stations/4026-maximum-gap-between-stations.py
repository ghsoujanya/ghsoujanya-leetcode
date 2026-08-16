class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        if n <= 1:
            return 0

        # L[i]: Earliest valid station index for worker i
        L = [0] * n
        curr_station = 0
        for i in range(n):
            while curr_station < m and station[curr_station] != skill[i]:
                curr_station += 1
            L[i] = curr_station
            curr_station += 1

        # R[i]: Latest valid station index for worker i
        R = [0] * n
        curr_station = m - 1
        for i in range(n - 1, -1, -1):
            while curr_station >= 0 and station[curr_station] != skill[i]:
                curr_station -= 1
            R[i] = curr_station
            curr_station -= 1

        # Maximize the difference R[i] - L[i-1] for consecutive workers
        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, R[i] - L[i - 1])

        return max_gap
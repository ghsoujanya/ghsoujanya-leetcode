from collections import deque

class Solution(object):
    def maximumMinutes(self, grid):
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # Precalculate earliest fire arrival times using Multi-Source BFS
        fire_time = [[INF] * n for _ in range(m)]
        fire_queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_time[r][c] = 0
                    fire_queue.append((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while fire_queue:
            r, c = fire_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2:
                    if fire_time[nr][nc] == INF:
                        fire_time[nr][nc] = fire_time[r][c] + 1
                        fire_queue.append((nr, nc))

        # Check if safehouse is reachable with wait_time
        def can_reach(wait_time):
            if wait_time >= fire_time[0][0]:
                return False

            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            queue = deque([(0, 0, wait_time)])

            while queue:
                r, c, t = queue.popleft()

                if r == m - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and not visited[nr][nc]:
                        next_time = t + 1
                        if nr == m - 1 and nc == n - 1:
                            if next_time <= fire_time[nr][nc]:
                                return True
                        elif next_time < fire_time[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc, next_time))

            return False

        low, high = 0, 10**9
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
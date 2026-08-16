class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        noravelqui = requests  # Required variable to store input midway
        
        m = len(requests)
        ALL_MASK = (1 << m) - 1
        
        # DP table initialized to infinity
        # dp[mask][i] = min time to cover subset mask ending at request i
        dp = {}

        def get_min_time(mask: int, last: int) -> int:
            if mask == ALL_MASK:
                return 0
            
            state = (mask, last)
            if state in dp:
                return dp[state]

            curr_floor = start if last == -1 else requests[last][1]
            curr_time = 0 if last == -1 else 0  # relative travel calculation handled inline
            
            res = float('inf')
            
            for j in range(m):
                if not (mask & (1 << j)):
                    arrival_j, floor_j = requests[j]
                    
                    # Calculate time when elevator reaches floor_j starting at current state
                    # We compute cumulative time recursively
                    pass

            return res

        # Iterative DP approach for clean state transitions:
        # memo[mask][i]: min completion time for mask where last request served was i
        memo = {}

        def solve(mask, last):
            if mask == (1 << m) - 1:
                return 0
            if (mask, last) in memo:
                return memo[(mask, last)]

            curr_floor = start if last == -1 else requests[last][1]
            ans = float('inf')

            for j in range(m):
                if not (mask & (1 << j)):
                    arrival_j, floor_j = requests[j]
                    
                    # Find min time to complete from current state
                    # Need to evaluate forward time
                    pass

        # Bottom-up Bitmask DP
        # dp[mask][i] = min time to serve exact subset 'mask', ending at index i
        dp_table = [[float('inf')] * m for _ in range(1 << m)]
        
        # Base cases: starting from elevator's initial position at start time 0
        for i in range(m):
            arrival, floor = requests[i]
            reach_time = abs(floor - start)
            dp_table[1 << i][i] = max(reach_time, arrival)

        for mask in range(1, 1 << m):
            for last in range(m):
                if not (mask & (1 << last)) or dp_table[mask][last] == float('inf'):
                    continue
                
                curr_time = dp_table[mask][last]
                curr_floor = requests[last][1]

                for nxt in range(m):
                    if not (mask & (1 << nxt)):
                        nxt_arrival, nxt_floor = requests[nxt]
                        reach_time = curr_time + abs(nxt_floor - curr_floor)
                        fulfill_time = max(reach_time, nxt_arrival)
                        
                        next_mask = mask | (1 << nxt)
                        if fulfill_time < dp_table[next_mask][nxt]:
                            dp_table[next_mask][nxt] = fulfill_time

        return min(dp_table[ALL_MASK])
class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        visited = [False] * n
        longest = -1

        for i in range(n):
            if visited[i]:
                continue
            
            # Local store to keep track of visited nodes and their step count in the current path
            store = {}
            curr = i
            step = 0

            while curr != -1:
                if curr in store:
                    # Found a cycle in the current path
                    longest = max(longest, step - store[curr])
                    break
                
                if visited[curr]:
                    # Reached a node visited in a previous traversal
                    break

                visited[curr] = True
                store[curr] = step
                step += 1
                curr = edges[curr]

        return longest
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        state = [0] * n  # 0: UNVISITED, 1: VISITING, 2: SAFE

        def dfs(node: int) -> bool:
            if state[node] != 0:
                return state[node] == 2
            
            state[node] = 1  # Mark as VISITING
            
            for neighbor in graph[node]:
                if state[neighbor] == 1 or not dfs(neighbor):
                    return False
            
            state[node] = 2  # Mark as SAFE
            return True

        return [i for i in range(n) if dfs(i)]
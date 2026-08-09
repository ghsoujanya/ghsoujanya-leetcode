from collections import defaultdict
from typing import List


class Solution:

  def criticalConnections(
      self, n: int, connections: List[List[int]]
  ) -> List[List[int]]:
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in connections:
      graph[u].append(v)
      graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = []
    timer = 0

    def dfs(node: int, parent: int):
      nonlocal timer
      disc[node] = low[node] = timer
      timer += 1

      for neighbor in graph[node]:
        if neighbor == parent:
          continue

        if disc[neighbor] != -1:
          # Neighbor is already visited (back-edge)
          low[node] = min(low[node], disc[neighbor])
        else:
          # Forward DFS
          dfs(neighbor, node)
          low[node] = min(low[node], low[neighbor])

          # If the lowest reachable node from neighbor is strictly greater than disc[node],
          # then (node, neighbor) is a critical connection.
          if low[neighbor] > disc[node]:
            bridges.append([node, neighbor])

    # Graph is connected, so one DFS from node 0 covers all nodes
    dfs(0, -1)
    return bridges
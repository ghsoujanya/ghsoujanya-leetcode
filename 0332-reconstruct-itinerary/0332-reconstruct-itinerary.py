import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Step 1: Construct graph with sorted adjacency lists (in reverse for efficient pop)
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        
        # Step 2: DFS using Hierholzer's Algorithm
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)
            
        dfs("JFK")
        
        # Step 3: Return reversed path
        return itinerary[::-1]
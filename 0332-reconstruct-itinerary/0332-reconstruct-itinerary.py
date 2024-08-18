class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets):
            adj[src].append(dest)
        
        result = []

        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop(0)
                dfs(next_dest)
            result.append(airport)

        dfs('JFK')

        return result[::-1]
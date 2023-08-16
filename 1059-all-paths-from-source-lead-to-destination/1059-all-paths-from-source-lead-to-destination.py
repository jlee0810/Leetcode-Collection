class Solution:
    GRAY = 1  # To detect cycle
    BLACK = 2 # Avoid unnecessary computation / already verified that all paths from node leads to destination

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])

        states = [None for _ in range(n)]

        def dfs(node):
            if states[node] is not None:
                return states[node] == self.BLACK
                # if the node's state is black we already know that all paths from node leads to destination
                # if the node's state is gray we know that there is a cycle
            if len(adj_list[node]) == 0:
                return node == destination
                # No neighbors means it must be the destination else it is false

            states[node] = self.GRAY

            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            
            states[node] = self.BLACK
            return True
        
        return dfs(source)

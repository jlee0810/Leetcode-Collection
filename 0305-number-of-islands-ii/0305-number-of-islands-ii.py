class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        num_islands = 0
        num_islands_results = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for position in positions:
            r, c = position

            if (r, c) in rank:
                num_islands_results.append(num_islands)
                continue

            parent[(r, c)] = (r, c)
            rank[(r, c)] = 1
            num_islands += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:
                    if find((nr, nc)) != find((r, c)):
                        union((nr, nc), (r, c))
                        num_islands -= 1
            
            num_islands_results.append(num_islands)
        
        return num_islands_results

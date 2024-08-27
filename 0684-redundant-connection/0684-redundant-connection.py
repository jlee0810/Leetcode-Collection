class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1 for _ in range(len(edges) + 1)]
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return True
            else:
                if rank[parent1] >= rank[parent2]:
                    parent[parent2] = parent[parent1]
                    rank[parent1] += rank[parent2]
                else:
                    parent[parent1] = parent[parent2]
                    rank[parent2] += rank[parent1]
                return False

        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
        return []
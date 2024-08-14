class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        def find(node):
            if parent[node] != node:
                return find(parent[node])
            else:
                return node
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return
            else:
                if rank[parent1] >= rank[parent2]:
                    parent[parent2] = parent[parent1]
                    rank[parent1] += rank[parent2]
                else:
                    parent[parent1] = parent[parent2]
                    rank[parent2] += rank[parent1]

        for n1, n2 in edges:
            union(n1, n2)
        
        s_parent = set()
        for i in range(n):
            s_parent.add(find(i))

        return len(s_parent)
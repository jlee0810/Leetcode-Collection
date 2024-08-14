class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if node != parent[node]:
                return find(parent[node])
            else:
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
                return False

        s_parent = set()
        for i in range(n):
            s_parent.add(find(i))
        
        return len(s_parent) == 1
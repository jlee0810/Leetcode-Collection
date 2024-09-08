class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        def find(node):
            if node != parent[node]:
                return find(parent[node])
            return node

        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)

            if root_n1 != root_n2:
                if rank[root_n1] >= rank[root_n2]:
                    parent[root_n2] = parent[root_n1]
                    rank[root_n1] += rank[root_n2]
                else:
                    parent[root_n1] = parent[root_n2]
                    rank[root_n2] += rank[root_n1]

        for n1, n2 in edges:
            union(n1, n2)

        parent_set = set()
        for i in range(n):
            parent_set.add(find(i))
        
        return len(parent_set)
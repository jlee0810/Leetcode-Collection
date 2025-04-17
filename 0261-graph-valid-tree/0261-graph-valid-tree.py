class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if node != parent[node]:
                node = find(parent[node])
            return node
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return True
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return False
                
        s_parent = set()
        for i in range(n):
            s_parent.add(find(i))

        return len(s_parent) == 1
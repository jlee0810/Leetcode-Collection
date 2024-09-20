from collections import defaultdict

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        good = 0

        def dfs(node, parent):
            nonlocal good
            size = 1
            child_sizes = []

            for nei in adj_list[node]:
                if nei != parent:
                    subtree_size = dfs(nei, node)
                    child_sizes.append(subtree_size)
                    size += subtree_size

            if len(set(child_sizes)) <= 1:
                good += 1

            return size

        dfs(0, -1)
        return good

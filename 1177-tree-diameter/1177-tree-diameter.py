class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        max_diam = 0

        def dfs(node, parent):
            nonlocal max_diam
            first_max, second_max = 0, 0

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    diam = dfs(neighbor, node)
                    if diam > first_max:
                        first_max, second_max = diam, first_max
                    elif diam > second_max:
                        second_max = diam

            max_diam = max(max_diam, first_max + second_max)

            return first_max + 1

        dfs(0, None)
        return max_diam
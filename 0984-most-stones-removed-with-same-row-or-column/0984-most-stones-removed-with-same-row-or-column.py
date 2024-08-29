class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        adj_list = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        num_of_connected_components = 0
        visited = [False] * n

        def dfs(stone):
            visited[stone] = True
            for nei in adj_list[stone]:
                if not visited[nei]:
                    dfs(nei)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                num_of_connected_components += 1
        return n - num_of_connected_components
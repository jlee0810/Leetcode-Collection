class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        island_signature = set()

        def dfs(r, c, direction, signature):
            nonlocal visited
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                grid[r][c] == 0 or
                (r, c) in visited):
                return
            
            visited.add((r, c))
            signature.append(direction)

            dfs(r - 1, c, 'U', signature)
            dfs(r + 1, c, 'D', signature)
            dfs(r, c - 1, 'L', signature)
            dfs(r, c + 1, 'R', signature)

            signature.append('B')

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    signature = []
                    dfs(i, j, 'O', signature)
                    island_signature.add(tuple(signature))

        return len(island_signature)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j, cache):
            if (i, j) in cache:
                return cache[(i, j)]
            
            max_val = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[i][j] < matrix[ni][nj]:
                    max_val = max(max_val, dfs(ni, nj, cache))
            cache[(i, j)] = max_val + 1
            return cache[(i, j)]

        max_path = 1
        cache = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(max_path, dfs(i, j, cache))

        return max_path
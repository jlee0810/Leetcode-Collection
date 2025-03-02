class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        def dfs(i, j):
            nonlocal cache

            if (i, j) in cache:
                return cache[(i, j)]

            max_val = 0

            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[i][j] < matrix[ni][nj]:
                    max_val = max(max_val, dfs(ni, nj))

            cache[(i, j)] = max_val + 1
            return max_val + 1

        longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path

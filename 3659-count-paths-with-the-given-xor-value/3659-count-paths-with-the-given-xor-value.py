class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[defaultdict(int) for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1

        for r in range(m):
            for c in range(n):
                for curr, cnt in dp[r][c].items():
                    if r + 1 < m:
                        new_val = curr ^ grid[r + 1][c]
                        dp[r + 1][c][new_val] = (dp[r + 1][c][new_val] + cnt) % MOD
                    if c + 1 < n:
                        new_val = curr ^ grid[r][c + 1]
                        dp[r][c + 1][new_val] = (dp[r][c + 1][new_val] + cnt) % MOD

        return dp[m - 1][n - 1].get(k, 0) % MOD
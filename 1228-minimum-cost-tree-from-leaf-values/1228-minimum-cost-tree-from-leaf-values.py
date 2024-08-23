class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        max_leaf = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            max_leaf[i][i] = arr[i]
            for j in range(i + 1, n):
                max_leaf[i][j] = max(max_leaf[i][j - 1], arr[j])
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + max_leaf[i][k] * max_leaf[k + 1][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n - 1]

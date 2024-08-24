class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0  # There's no cost if there's only one leaf node
            min_cost = float('inf')
            for k in range(i, j):
                left_max = max(arr[i:k+1])
                right_max = max(arr[k+1:j+1])
                cost = dp(i, k) + dp(k + 1, j) + left_max * right_max
                min_cost = min(min_cost, cost)
            return min_cost
        
        return dp(0, len(arr) - 1)


















        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # max_leaf = [[0 for _ in range(n)] for _ in range(n)]

        # for i in range(n):
        #     max_leaf[i][i] = arr[i]
        #     for j in range(i + 1, n):
        #         max_leaf[i][j] = max(max_leaf[i][j - 1], arr[j])
        
        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1
        #         dp[i][j] = float('inf')
        #         for k in range(i, j):
        #             cost = dp[i][k] + dp[k + 1][j] + max_leaf[i][k] * max_leaf[k + 1][j]
        #             dp[i][j] = min(dp[i][j], cost)
        
        # return dp[0][n - 1]

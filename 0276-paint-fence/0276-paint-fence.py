class Solution:
    def numWays(self, n: int, k: int) -> int:
        #Different color: (k - 1) * (dp[i - 1])
        #Same color: 1 * dp[i - 1] but the dp[i - 1] has to be different color than dp[i - 2]
        #Combining these findings 1 * (k - 1) * dp[i - 2]

        if n == 1:
            return k 
            
        dp = [0 for _ in range(n + 1)] 
        dp[1], dp[2] = k, k ** 2

        for i in range(3, n + 1):
            dp[i] = (k - 1) * dp[i - 1] + (k - 1) * dp[i - 2]

        return dp[-1]
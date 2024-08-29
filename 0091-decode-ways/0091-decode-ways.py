class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # dp[i] means number of ways to decode S[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string can be decoded in one way
        
        for i in range(1, n + 1):
            # Check single digit decode option
            if s[i-1] != '0':  # Cannot decode a single '0'
                dp[i] += dp[i-1]
            
            # Check two digits decode option
            if i > 1 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        
        return dp[n] 
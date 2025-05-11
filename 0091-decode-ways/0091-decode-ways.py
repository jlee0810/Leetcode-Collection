class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        if not s or s[0] == "0":
            return 0

        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        for i in range(1, len(s)):
            if s[i - 1] != "0":
                if 1 <= int(s[i - 1 : i + 1]) <= 26:
                    dp[i] += dp[i - 2] if i >= 2 else 1
            if s[i] != "0":
                dp[i] += dp[i - 1]

        return dp[-1]

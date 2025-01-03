class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i - 1] != "0":
                two_digit = s[i - 1 : i + 1]
                if 1 <= int(two_digit) <= 26:
                    dp[i] += dp[i - 2] if i >= 2 else 1

            if s[i] != "0":
                dp[i] += dp[i - 1]

        return dp[-1]

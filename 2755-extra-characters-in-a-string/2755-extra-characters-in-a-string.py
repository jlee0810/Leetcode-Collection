class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)

        for start in range(len(s) - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if substring in dictionary:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
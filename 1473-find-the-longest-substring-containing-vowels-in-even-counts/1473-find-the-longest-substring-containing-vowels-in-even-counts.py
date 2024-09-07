class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        dp = {0:-1}
        parity = 0
        ans = 0
        vowels = "aeiou"

        for i, c in enumerate(s):
            if c in vowels:
                index = vowels.index(c)
                parity ^= 1 << index
            if parity in dp:
                ans = max(ans, i - dp[parity])
            else:
                dp[parity] = i
        
        return ans
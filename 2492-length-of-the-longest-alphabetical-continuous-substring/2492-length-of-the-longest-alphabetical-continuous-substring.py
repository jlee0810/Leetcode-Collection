class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_string = 1
        l = 0
        for r in range(1, len(s)):
            if ord(s[r]) - ord(s[r - 1]) == 1:
                max_string = max(max_string, r - l + 1)
                continue
            else:
                l = r
        return max_string
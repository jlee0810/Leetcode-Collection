class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0

        cnt = Counter(s)

        for idx, c in enumerate(s):
            if cnt[c] < k:
                left = self.longestSubstring(s[:idx], k)
                right = self.longestSubstring(s[idx+1:], k)
                return max(left, right)
            
        return len(s)
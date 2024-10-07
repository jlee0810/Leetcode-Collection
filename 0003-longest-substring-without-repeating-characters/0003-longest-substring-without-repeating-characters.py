class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sset = set()

        l = 0
        
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            max_length = max(max_length, r - l + 1)
            sset.add(s[r])
        
        return max_length

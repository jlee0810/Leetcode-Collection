class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while 0 <= l and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > len(longest):
                        longest= s[l : r + 1]
                    l -= 1
                    r += 1

        return longest
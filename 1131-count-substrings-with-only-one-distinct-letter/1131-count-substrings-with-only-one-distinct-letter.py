class Solution:
    def countLetters(self, s: str) -> int:
        count = 0
        l = 0

        for r in range(len(s) + 1):
            if r == len(s) or s[l] != s[r]:
                length = r - l
                count += (1 + length) * length // 2
                l = r
        return count

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        last_idx = 0
        power = 1
        mod = 10 ** 9 + 7

        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod

            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last_idx = i
        
        suffix = s[last_idx + 1:]
        return suffix[::-1] + s
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        current = {}
        needed = Counter(t)

        l = 0
        result, min_length = "", float('inf')
        have, need = 0, len(needed)

        for r in range(len(s)):
            if s[r] in needed:
                current[s[r]] = current.get(s[r], 0) + 1
                if current[s[r]] == needed[s[r]]:
                    have += 1
            while have == need:
                if r - l + 1 < min_length: 
                    result = s[l : r + 1]
                    min_length = r - l + 1
                if s[l] in needed:
                    current[s[l]] -= 1
                    if current[s[l]] < needed[s[l]]:
                        have -= 1
                l += 1

        return result

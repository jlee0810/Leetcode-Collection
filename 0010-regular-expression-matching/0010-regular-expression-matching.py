class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            current_char_match = i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == ".")

            # * regex mathching
            if j + 1 < len(p) and p[j + 1] == '*':
                # matches zero + more of the preceding element
                cache[(i, j)] = dp(i, j + 2) or (current_char_match and dp(i + 1, j))
                return cache[(i, j)]
                
            # no special character
            if current_char_match:
                cache[(i, j)] = dp(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
        
        return dp(0, 0)
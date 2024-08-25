class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        result = 0
        
        def countDifferentByOne(s: str, t: str) -> int:
            count = 0
            m, n = len(s), len(t)
            for i in range(m):
                for j in range(n):
                    mismatches = 0
                    k = 0
                    while i + k < m and j + k < n:
                        if s[i + k] != t[j + k]:
                            mismatches += 1
                        if mismatches == 1:
                            count += 1
                        elif mismatches > 1:
                            break
                        k += 1
            return count
        
        result = countDifferentByOne(s, t)
        
        return result
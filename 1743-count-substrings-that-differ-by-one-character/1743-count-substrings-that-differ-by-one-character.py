class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if len(s) > len(t):
            return -1

        result = 0
        
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                substr_s = s[i:i + length]
                for j in range(len(t) - length + 1):
                    substr_t = t[j:j + length]
                    differ = 0
                    
                    for k in range(length):
                        if substr_s[k] != substr_t[k]:
                            differ += 1
                        if differ > 1:
                            break
                    
                    if differ == 1:
                        result += 1
        
        return result
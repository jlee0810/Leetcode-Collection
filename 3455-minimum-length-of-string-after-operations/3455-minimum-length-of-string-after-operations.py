class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        result = 0

        for key, val in c.items():
            while val >= 3:
                val -= 2
            result += val
        
        return result
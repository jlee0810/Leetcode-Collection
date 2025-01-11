class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        c = Counter(s)
        count = 0
        for key, val in c.items():
            if val % 2 != 0:
                count += 1

        if count > k:
            return False

        return True

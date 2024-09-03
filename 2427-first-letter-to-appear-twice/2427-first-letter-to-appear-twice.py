class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sset = set()
        for c in s:
            if c in sset:
                return c
            sset.add(c)
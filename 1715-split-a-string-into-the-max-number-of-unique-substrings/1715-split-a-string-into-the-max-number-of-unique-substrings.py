class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_split = 0

        def backtrack(idx, sset, split):
            nonlocal max_split
            if idx == len(s):
                max_split = max(max_split, len(sset))
                return
            
            for i in range(idx, len(s)):
                substr = s[idx: i + 1]
                if substr in sset:
                    continue
                sset.add(substr)
                backtrack(i + 1, sset, split + 1)
                sset.remove(substr)
        
        backtrack(0, set(), 0)
        return max_split
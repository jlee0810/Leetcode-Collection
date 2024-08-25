class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(idx, combo):
            if sum(combo) == target:
                result.append(combo.copy())
                return
            if idx >= len(candidates) or sum(combo) > target:
                return
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, combo)
                combo.pop()
                prev = candidates[i]
        
        backtrack(0, [])
        return result
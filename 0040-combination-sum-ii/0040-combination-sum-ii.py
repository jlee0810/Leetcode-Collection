class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(idx, combo):
            if sum(combo) == target:
                result.append(combo.copy())
                return
            if sum(combo) > target or idx >= len(candidates):
                return
            prev = float('-inf')
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                # include this candidate
                combo.append(candidates[i])
                backtrack(i + 1, combo)
                # not include
                combo.pop()
                prev = candidates[i]

        backtrack(0, [])
        return result
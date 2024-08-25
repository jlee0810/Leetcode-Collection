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
            combo.append(candidates[idx])
            backtrack(idx + 1, combo)
            combo.pop()
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            backtrack(idx + 1, combo)

    
        backtrack(0, [])
        return result
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, combo):
            if sum(combo) == target:
                result.append(combo.copy())
                return 
            if sum(combo) > target:
                return
            for i in range(idx, len(candidates)):
                combo.append(candidates[i])
                backtrack(i, combo)
                combo.pop()

        backtrack(0, [])

        return result
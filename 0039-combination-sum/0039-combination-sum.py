class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, combo):
            if sum(combo) == target:
                result.append(combo.copy())
                return
            if sum(combo) > target:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                dfs(i, combo)
                combo.pop()
        
        dfs(0, [])
        return result
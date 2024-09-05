class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c, target+1):
                if i == c: 
                    dp[i].append([c])
                for comb in dp[i-c]: 
                    dp[i].append(comb + [c])
        return dp[-1]
        
        # result = []

        # def backtrack(idx, combo):
        #     if sum(combo) == target:
        #         result.append(combo.copy())
        #         return 
        #     if sum(combo) > target:
        #         return
        #     for i in range(idx, len(candidates)):
        #         combo.append(candidates[i])
        #         backtrack(i, combo)
        #         combo.pop()

        # backtrack(0, [])

        # return result
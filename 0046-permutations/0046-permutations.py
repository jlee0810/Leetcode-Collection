class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, p):
            if idx == len(nums):
                result.append(p.copy())
                return
            for i in range(idx, len(nums)):
                p[idx], p[i] = p[i], p[idx]
                backtrack(idx + 1, p)
                p[idx], p[i] = p[i], p[idx]

        backtrack(0, nums)

        return result

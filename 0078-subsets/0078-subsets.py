class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, subset):
            nonlocal result
            if idx == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()
            backtrack(idx + 1, subset)
        
        backtrack(0, [])

        return result
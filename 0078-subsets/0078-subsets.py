class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start, subset):
            if start >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[start])
            dfs(start + 1, subset)
            subset.pop()
            dfs(start + 1, subset)
        dfs(0, [])   
        return result
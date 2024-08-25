class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
                idx += 1
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return result
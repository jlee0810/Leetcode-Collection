class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, sub):
            if idx == len(nums):
                result.append(sub.copy())
                return
            sub.append(nums[idx])
            backtrack(idx + 1, sub)
            sub.pop()
            backtrack(idx + 1, sub)
        backtrack(0, [])
        return result
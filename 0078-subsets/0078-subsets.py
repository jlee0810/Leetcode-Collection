class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, ss):
            if idx == len(nums):
                result.append(ss.copy())
                return
            ss.append(nums[idx])
            backtrack(idx + 1, ss)
            ss.pop()
            backtrack(idx + 1, ss)

        backtrack(0, [])

        return result